from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    groups_owned = db.relationship('Group', backref='owner', lazy=True)
    memberships = db.relationship('GroupMember', backref='user', lazy=True)
    expenses_paid = db.relationship('Expense', backref='paid_by_user', lazy=True, foreign_keys='Expense.paid_by_user_id')
    shares = db.relationship('ExpenseShare', backref='user', lazy=True)
    settlements_from = db.relationship('Settlement', foreign_keys='Settlement.from_user_id', backref='from_user', lazy=True)
    settlements_to = db.relationship('Settlement', foreign_keys='Settlement.to_user_id', backref='to_user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return self.password_hash and check_password_hash(self.password_hash, password)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    memberships = db.relationship('GroupMember', backref='group', lazy=True, cascade='all, delete-orphan')
    expenses = db.relationship('Expense', backref='group', lazy=True, cascade='all, delete-orphan')
    settlements = db.relationship('Settlement', backref='group', lazy=True, cascade='all, delete-orphan')

class GroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    joined_at = db.Column(db.Date, nullable=False)
    left_at = db.Column(db.Date, nullable=True)

    def is_active_on(self, when):
        return self.joined_at <= when and (self.left_at is None or self.left_at >= when)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    paid_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    raw_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False, default='INR')
    amount_in_base = db.Column(db.Float, nullable=False)
    split_type = db.Column(db.String(30), nullable=False)
    split_details = db.Column(db.String(500), nullable=True)
    notes = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    shares = db.relationship('ExpenseShare', backref='expense', lazy=True, cascade='all, delete-orphan')

class ExpenseShare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense_id = db.Column(db.Integer, db.ForeignKey('expense.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    share_description = db.Column(db.String(200), nullable=True)

class Settlement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    from_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    to_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False, default='INR')
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
