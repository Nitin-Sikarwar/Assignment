import csv
from utils import parse_date_safe, parse_amount, parse_participants, compute_expense_shares
import codecs

REPORT_FILE = 'IMPORT_REPORT.md'

with codecs.open('Expenses Export.csv', 'r', 'utf-8') as f:
    rows = list(csv.DictReader(f, skipinitialspace=True))

seen = set()
lines = ['# Import Report\n', 'This report was generated from `Expenses Export.csv` using the app import logic.\n', '']
for i, row in enumerate(rows, 1):
    date_raw = row.get('date')
    date, err = parse_date_safe(date_raw)
    amount = parse_amount(row.get('amount'))
    currency = (row.get('currency') or 'INR').upper()
    split_type = (row.get('split_type') or '').strip().lower()
    participants = parse_participants(row.get('split_with'))
    split_details = row.get('split_details', '')
    st = 'settlement' if not split_type and len(participants) == 1 else (split_type or 'equal')
    shares, errs = compute_expense_shares(st, amount if currency == 'INR' else amount * 83.0, participants, split_details)
    key = (
        date_raw.strip() if date_raw else '',
        (row.get('description') or '').strip().lower(),
        (row.get('paid_by') or '').strip().lower(),
        round(amount, 2),
        currency,
        st,
        ';'.join(sorted(participants)),
    )
    dup = key in seen
    seen.add(key)
    anomaly = []
    if err:
        anomaly.append(f'Invalid date: {err}')
    if amount == 0 and (row.get('amount') or '').strip() != '0':
        anomaly.append('Amount parse failed or empty')
    if currency == '':
        anomaly.append('Missing currency, defaulting to INR')
    if row.get('currency', '').strip() == '':
        anomaly.append('Currency blank')
    if not row.get('paid_by', '').strip():
        anomaly.append('Missing paid_by/payer value')
    if row.get('split_type', '') == '' and len(participants) != 1:
        anomaly.append('No split_type given, defaulting to equal')
    if st == 'settlement' and not row.get('split_type', '').strip():
        anomaly.append('Treated as settlement because split_type is blank and one payee is listed')
    if st == 'percentage' and any('percentage' in e.lower() for e in errs) and errs:
        anomaly.append('Percentage split details may be invalid')
    if st == 'unequal' and any('Unequal shares total' in e for e in errs):
        anomaly.append('Unequal split totals do not match amount')
    if st == 'share' and any('Share counts missing' in e for e in errs):
        anomaly.append('Share split count missing or invalid')
    if dup:
        anomaly.append('Duplicate candidate based on normalized row key')

    lines.append(f'## Row {i}: {row.get("description") or "<no description>"}')
    lines.append(f'- Raw CSV: {row}')
    lines.append(f'- Parsed date: {date_raw!r} -> {date!r}')
    lines.append(f'- Amount: {row.get("amount")} {currency} -> {amount} in {currency}')
    lines.append(f'- Split type: {st}')
    lines.append(f'- Participants: {participants}')
    lines.append(f'- Split details: {split_details}')
    lines.append(f'- Computed shares: {shares}')
    if anomaly:
        lines.append(f'- Anomalies:')
        for note in anomaly:
            lines.append(f'  - {note}')
    else:
        lines.append('- Anomalies: none')
    if errs:
        lines.append(f'- Parser errors: {errs}')
    lines.append('')

with open(REPORT_FILE, 'w', encoding='utf-8') as outf:
    outf.write('\n'.join(lines))
print(f'Wrote {REPORT_FILE}')
