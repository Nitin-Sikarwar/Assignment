import csv
import re
from datetime import datetime, date
from dateutil.parser import parse as parse_date

DEFAULT_CURRENCY = 'INR'
USD_TO_INR_RATE = 83.0

SPLIT_TYPES = {'equal', 'percentage', 'unequal', 'share'}

NAME_SPLIT_RE = re.compile(r"\s*;\s*")
ITEM_SPLIT_RE = re.compile(r"\s*;\s*")
ENTRY_RE = re.compile(r"^(?P<name>[^0-9%]+?)\s*(?P<value>[0-9.,%]+)$")


def normalize_name(name):
    if not name:
        return ''
    return name.strip().title()


def parse_amount(amount_text):
    if amount_text is None:
        return 0.0
    text = str(amount_text).strip().replace(',', '')
    if text == '':
        return 0.0
    try:
        return float(text)
    except ValueError:
        return 0.0


def parse_date_safe(raw_text):
    if not raw_text:
        return None, 'Missing date'
    raw_text = raw_text.strip()
    try:
        dt = parse_date(raw_text, dayfirst=True, fuzzy=False)
        if dt.year < 1900:
            dt = dt.replace(year=2026)
        return dt.date(), None
    except Exception as exc:
        return None, f'Could not parse date: {exc}'


def parse_participants(raw):
    if not raw:
        return []
    return [normalize_name(name) for name in NAME_SPLIT_RE.split(raw) if name.strip()]


def parse_split_map(raw):
    shares = {}
    if not raw:
        return shares
    parts = ITEM_SPLIT_RE.split(raw)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        tokens = part.split()
        if len(tokens) < 2:
            continue
        name = normalize_name(' '.join(tokens[:-1]))
        value = tokens[-1].strip()
        shares[name] = value
    return shares


def convert_currency(amount, currency):
    if not currency or currency.upper() == DEFAULT_CURRENCY:
        return amount, DEFAULT_CURRENCY
    if currency.upper() == 'USD':
        return amount * USD_TO_INR_RATE, DEFAULT_CURRENCY
    return amount, currency.upper()


def compute_expense_shares(split_type, amount, participants, split_details):
    if not participants:
        return {}, ['No participants']
    shares = {}
    errors = []
    count = len(participants)
    if split_type == 'equal' or split_type == '':
        per = round(amount / count, 2) if count else 0.0
        for participant in participants:
            shares[participant] = per
    elif split_type == 'percentage':
        share_map = parse_split_map(split_details)
        total = 0.0
        for name, value in share_map.items():
            value = value.strip().rstrip('%')
            try:
                percent = float(value)
                shares[name] = round(amount * percent / 100.0, 2)
                total += percent
            except ValueError:
                errors.append(f'Invalid percentage for {name}: {value}')
        if abs(total - 100.0) > 1.0:
            errors.append(f'Percentages do not sum to 100 ({total}%)')
        for participant in participants:
            shares.setdefault(participant, 0.0)
    elif split_type == 'unequal':
        share_map = parse_split_map(split_details)
        total = 0.0
        for name, value in share_map.items():
            amt = parse_amount(value)
            shares[name] = amt
            total += amt
        if abs(total - amount) > 1.0:
            errors.append(f'Unequal shares total {total} vs amount {amount}')
        for participant in participants:
            shares.setdefault(participant, 0.0)
    elif split_type == 'share':
        share_map = parse_split_map(split_details)
        total_shares = 0
        for name, value in share_map.items():
            try:
                total_shares += int(value)
                shares[name] = int(value)
            except ValueError:
                errors.append(f'Invalid share count for {name}: {value}')
        if total_shares == 0:
            errors.append('Share counts missing or zero')
        else:
            for name, count_value in list(shares.items()):
                shares[name] = round(amount * count_value / total_shares, 2)
        for participant in participants:
            shares.setdefault(participant, 0.0)
    else:
        errors.append(f'Unsupported split type {split_type}')
        for participant in participants:
            shares[participant] = 0.0
    return shares, errors


def normalize_expense_key(row):
    return (
        row['date'].isoformat() if row.get('date') else None,
        row.get('description', '').strip().lower(),
        normalize_name(row.get('paid_by', '')),
        round(parse_amount(row.get('amount', 0.0)), 2),
        (row.get('currency') or DEFAULT_CURRENCY).upper(),
        (row.get('split_type') or '').strip().lower(),
        ';'.join(sorted(parse_participants(row.get('split_with', ''))))
    )


def load_csv_rows(file_stream):
    reader = csv.DictReader((line.decode('utf-8-sig') for line in file_stream), skipinitialspace=True)
    rows = []
    for row in reader:
        rows.append(row)
    return rows
