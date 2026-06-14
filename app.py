import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User, Group, GroupMember, Expense, ExpenseShare, Settlement
from utils import (
    normalize_name,
    parse_amount,
    parse_date_safe,
    parse_participants,
    convert_currency,
    compute_expense_shares,
    normalize_expense_key,
    load_csv_rows,
    SPLIT_TYPES,
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shared_expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'replace-this-with-a-secret'

db.init_app(app)

with app.app_context():
    db.create_all()


def current_user():
    user_id = session.get('user_id')
    if not user_id:
        return None
    return User.query.get(user_id)

@app.context_processor
def inject_user():
    return {'current_user': current_user()}


def login_required(fn):
    from functools import wraps

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user():
            flash('Login required', 'warning')
            return redirect(url_for('login'))
        return fn(*args, **kwargs)

    return wrapper


def active_group_members(group, when=None):
    if when is None:
        when = datetime.utcnow().date()
    members = []
    for m in group.memberships:
        if m.is_active_on(when):
            members.append(m.user)
    return members


def get_group_balances(group):
    balances = {}
    members = {m.user.id: m.user for m in group.memberships}
    for user in members.values():
        balances[user.id] = {'user': user, 'paid': 0.0, 'owed': 0.0, 'net': 0.0}

    for expense in group.expenses:
        payer_id = expense.paid_by_user_id
        balances.setdefault(payer_id, {'user': expense.paid_by_user, 'paid': 0.0, 'owed': 0.0, 'net': 0.0})
        balances[payer_id]['paid'] += expense.amount_in_base
        for share in expense.shares:
            balances.setdefault(share.user_id, {'user': share.user, 'paid': 0.0, 'owed': 0.0, 'net': 0.0})
            balances[share.user_id]['owed'] += share.amount
    for settlement in group.settlements:
        balances.setdefault(settlement.from_user_id, {'user': settlement.from_user, 'paid': 0.0, 'owed': 0.0, 'net': 0.0})
        balances.setdefault(settlement.to_user_id, {'user': settlement.to_user, 'paid': 0.0, 'owed': 0.0, 'net': 0.0})
        balances[settlement.to_user_id]['net'] += settlement.amount
        balances[settlement.from_user_id]['net'] -= settlement.amount
    for user_id, state in balances.items():
        state['net'] += state['paid'] - state['owed']
    return balances


def settlement_suggestions(balances):
    owes = []
    owed = []
    for user_id, state in balances.items():
        net = round(state['net'], 2)
        if net < -0.01:
            owes.append({'user': state['user'], 'amount': -net})
        elif net > 0.01:
            owed.append({'user': state['user'], 'amount': net})
    owes.sort(key=lambda x: x['amount'])
    owed.sort(key=lambda x: x['amount'], reverse=True)
    instructions = []
    i = 0
    j = 0
    while i < len(owes) and j < len(owed):
        payer = owes[i]
        receiver = owed[j]
        amount = min(payer['amount'], receiver['amount'])
        if amount > 0.01:
            instructions.append({'from': payer['user'], 'to': receiver['user'], 'amount': round(amount, 2)})
        payer['amount'] -= amount
        receiver['amount'] -= amount
        if payer['amount'] < 0.01:
            i += 1
        if receiver['amount'] < 0.01:
            j += 1
    return instructions


def find_or_create_user(name):
    username = normalize_name(name)
    if not username:
        return None
    user = User.query.filter_by(username=username).first()
    if user:
        return user
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return user


def parse_import_row(row, group, creator):
    date_value, date_error = parse_date_safe(row.get('date'))
    paid_by_name = normalize_name(row.get('paid_by'))
    amount = parse_amount(row.get('amount'))
    currency = (row.get('currency') or 'INR').upper()
    amount_in_base, base_currency = convert_currency(amount, currency)
    split_type = (row.get('split_type') or '').strip().lower()
    participants = parse_participants(row.get('split_with'))
    is_settlement = not split_type and len(participants) == 1
    if not split_type and not is_settlement:
        split_type = 'equal'
    shares, parse_errors = compute_expense_shares(split_type, amount_in_base, participants, row.get('split_details', ''))
    if is_settlement:
        shares = {}
        split_type = 'settlement'
    return {
        'date': date_value.isoformat() if date_value else None,
        'date_error': date_error,
        'description': row.get('description', '').strip(),
        'paid_by': paid_by_name,
        'amount': amount,
        'currency': currency,
        'amount_in_base': amount_in_base,
        'split_type': split_type,
        'split_with': participants,
        'shares': shares,
        'split_details': row.get('split_details', '').strip(),
        'notes': row.get('notes', '').strip(),
        'errors': parse_errors,
        'raw': {
            'date': row.get('date'),
            'description': row.get('description'),
            'paid_by': row.get('paid_by'),
            'amount': row.get('amount'),
            'currency': row.get('currency'),
            'split_type': row.get('split_type'),
            'split_with': row.get('split_with'),
            'split_details': row.get('split_details'),
            'notes': row.get('notes'),
        },
    }

@app.route('/')
def home():
    if current_user():
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = normalize_name(request.form.get('username'))
        email = request.form.get('email', '').strip().lower() or None
        password = request.form.get('password', '')
        if not username or not password:
            flash('Please provide username and password.', 'danger')
            return redirect(url_for('register'))
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        flash('Account created.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = normalize_name(request.form.get('username'))
        password = request.form.get('password', '')
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash('Invalid credentials.', 'danger')
            return redirect(url_for('login'))
        session['user_id'] = user.id
        flash('Logged in successfully.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = current_user()
    groups = Group.query.filter((Group.owner == user) | (Group.memberships.any(user_id=user.id))).all()
    return render_template('dashboard.html', user=user, groups=groups)

@app.route('/groups/new', methods=['GET', 'POST'])
@login_required
def create_group():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        members_text = request.form.get('members', '').strip()
        if not name:
            flash('Group name required', 'danger')
            return redirect(url_for('create_group'))
        group = Group(name=name, owner_id=current_user().id)
        db.session.add(group)
        db.session.commit()
        if members_text:
            for name_text in members_text.split(','):
                name_norm = normalize_name(name_text)
                if not name_norm:
                    continue
                member = find_or_create_user(name_norm)
                if member and not GroupMember.query.filter_by(group_id=group.id, user_id=member.id).first():
                    gm = GroupMember(group_id=group.id, user_id=member.id, joined_at=datetime.utcnow().date())
                    db.session.add(gm)
            db.session.commit()
        flash('Group created.', 'success')
        return redirect(url_for('group_detail', group_id=group.id))
    return render_template('create_group.html')

@app.route('/group/<int:group_id>')
@login_required
def group_detail(group_id):
    group = Group.query.get_or_404(group_id)
    balances = get_group_balances(group)
    instructions = settlement_suggestions(balances)
    memberships = sorted(group.memberships, key=lambda m: m.joined_at)
    return render_template('group_detail.html', group=group, balances=balances, instructions=instructions, memberships=memberships)

@app.route('/group/<int:group_id>/members', methods=['POST'])
@login_required
def add_member(group_id):
    group = Group.query.get_or_404(group_id)
    name = normalize_name(request.form.get('member_name'))
    joined_at_str = request.form.get('joined_at')
    left_at_str = request.form.get('left_at')
    if not name or not joined_at_str:
        flash('Member name and joined date required.', 'danger')
        return redirect(url_for('group_detail', group_id=group.id))
    member_user = find_or_create_user(name)
    joined_at, _ = parse_date_safe(joined_at_str)
    left_at, _ = parse_date_safe(left_at_str) if left_at_str else (None, None)
    if not joined_at:
        flash('Invalid join date.', 'danger')
        return redirect(url_for('group_detail', group_id=group.id))
    gm = GroupMember(group_id=group.id, user_id=member_user.id, joined_at=joined_at, left_at=left_at)
    db.session.add(gm)
    db.session.commit()
    flash('Member added.', 'success')
    return redirect(url_for('group_detail', group_id=group.id))

@app.route('/group/<int:group_id>/expense/new', methods=['GET', 'POST'])
@login_required
def add_expense(group_id):
    group = Group.query.get_or_404(group_id)
    if request.method == 'POST':
        date_value, date_error = parse_date_safe(request.form.get('date'))
        description = request.form.get('description', '').strip()
        paid_by_name = normalize_name(request.form.get('paid_by'))
        amount = parse_amount(request.form.get('amount'))
        currency = (request.form.get('currency') or 'INR').upper()
        split_type = (request.form.get('split_type') or 'equal').strip().lower()
        split_with = request.form.get('split_with')
        split_details = request.form.get('split_details')
        notes = request.form.get('notes')
        participants = parse_participants(split_with)
        if not date_value or not description or not paid_by_name or amount <= 0:
            flash('Complete all required fields.', 'danger')
            return redirect(url_for('add_expense', group_id=group.id))
        paid_by = find_or_create_user(paid_by_name)
        amount_in_base, _ = convert_currency(amount, currency)
        shares, errors = compute_expense_shares(split_type, amount_in_base, participants, split_details)
        expense = Expense(
            group_id=group.id,
            created_by_id=current_user().id,
            date=date_value,
            description=description,
            paid_by_user_id=paid_by.id,
            raw_amount=amount,
            currency=currency,
            amount_in_base=amount_in_base,
            split_type=split_type,
            split_details=split_details,
            notes=notes,
        )
        db.session.add(expense)
        db.session.flush()
        for participant_name, share_amount in shares.items():
            participant = find_or_create_user(participant_name)
            if not participant:
                continue
            lo = ExpenseShare(expense_id=expense.id, user_id=participant.id, amount=share_amount, share_description=participant_name)
            db.session.add(lo)
        db.session.commit()
        flash('Expense added.', 'success')
        return redirect(url_for('group_detail', group_id=group.id))
    return render_template('add_expense.html', group=group, split_types=SPLIT_TYPES)

@app.route('/group/<int:group_id>/settle', methods=['POST'])
@login_required
def add_settlement(group_id):
    group = Group.query.get_or_404(group_id)
    from_user_name = normalize_name(request.form.get('from_user'))
    to_user_name = normalize_name(request.form.get('to_user'))
    amount = parse_amount(request.form.get('amount'))
    date_value, date_error = parse_date_safe(request.form.get('date'))
    notes = request.form.get('notes')
    if not from_user_name or not to_user_name or amount <= 0 or not date_value:
        flash('Fill settlement details.', 'danger')
        return redirect(url_for('group_detail', group_id=group.id))
    from_user = find_or_create_user(from_user_name)
    to_user = find_or_create_user(to_user_name)
    settlement = Settlement(group_id=group.id, from_user_id=from_user.id, to_user_id=to_user.id, amount=amount, currency='INR', date=date_value, notes=notes)
    db.session.add(settlement)
    db.session.commit()
    flash('Settlement recorded.', 'success')
    return redirect(url_for('group_detail', group_id=group.id))

@app.route('/group/<int:group_id>/import', methods=['GET', 'POST'])
@login_required
def import_csv(group_id):
    group = Group.query.get_or_404(group_id)
    if request.method == 'POST':
        file = request.files.get('csv_file')
        if not file:
            flash('Upload a CSV file.', 'danger')
            return redirect(url_for('import_csv', group_id=group.id))
        rows = load_csv_rows(file.stream)
        parsed = []
        duplicates = {}
        seen = set()
        for row in rows:
            item = parse_import_row(row, group, current_user())
            key = normalize_expense_key(item)
            if key in seen:
                duplicates[key] = duplicates.get(key, []) + [item]
            seen.add(key)
            parsed.append(item)
        session['import_rows'] = json.dumps(parsed, default=str)
        session['import_group_id'] = group.id
        return render_template('import_review.html', group=group, rows=parsed, duplicates=duplicates)
    return render_template('import_csv.html', group=group)

@app.route('/group/<int:group_id>/import/confirm', methods=['POST'])
@login_required
def confirm_import(group_id):
    group = Group.query.get_or_404(group_id)
    rows_json = session.get('import_rows')
    if not rows_json or session.get('import_group_id') != group.id:
        flash('No import session found. Re-upload the CSV.', 'danger')
        return redirect(url_for('import_csv', group_id=group.id))
    rows = json.loads(rows_json)
    for index, row in enumerate(rows):
        keep_flag = request.form.get(f'keep_{index}')
        if keep_flag is None:
            continue
        if row['date'] is None or not row['paid_by'] or row['amount'] <= 0:
            continue
        paid_by = find_or_create_user(normalize_name(row['paid_by']))
        if row['split_type'] == 'settlement' and row['split_with']:
            to_user = find_or_create_user(row['split_with'][0])
            settlement = Settlement(
                group_id=group.id,
                from_user_id=paid_by.id,
                to_user_id=to_user.id,
                amount=row['amount'],
                currency=row['currency'],
                date=datetime.fromisoformat(row['date']).date(),
                notes=row['notes'],
            )
            db.session.add(settlement)
            continue
        expense = Expense(
            group_id=group.id,
            created_by_id=current_user().id,
            date=datetime.fromisoformat(row['date']).date(),
            description=row['description'] or 'Imported expense',
            paid_by_user_id=paid_by.id,
            raw_amount=row['amount'],
            currency=row['currency'],
            amount_in_base=row['amount_in_base'],
            split_type=row['split_type'],
            split_details=row['split_details'],
            notes=row['notes'],
        )
        db.session.add(expense)
        db.session.flush()
        for participant_name, share_amount in row['shares'].items():
            participant = find_or_create_user(participant_name)
            if participant:
                db.session.add(ExpenseShare(expense_id=expense.id, user_id=participant.id, amount=share_amount, share_description=participant_name))
    db.session.commit()
    session.pop('import_rows', None)
    session.pop('import_group_id', None)
    flash('CSV imported into group.', 'success')
    return redirect(url_for('group_detail', group_id=group.id))

if __name__ == '__main__':
    app.run(debug=True)
