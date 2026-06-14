# Shared Expenses App

A Flask-based shared expenses tracker for flatmates.

## Features
- Login and registration
- Groups with membership join/leave timeline
- Expense creation and settlement recording
- Import `Expenses Export.csv` through the app
- Supports equal, percentage, unequal, and share splits
- Balance summary and suggested payment settlement instructions
- Duplicate detection and import review

## Run locally
1. Create a Python environment and install dependencies:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
2. Initialize the database and start the app:
   ```powershell
   python app.py
   ```
3. Open http://127.0.0.1:5000

## Importing the CSV
- Login, create a group, then use the group import page.
- The importer normalizes dates, currencies, and duplicate candidates.
- USD rows are converted to INR with a fixed exchange rate.

## Notes
- The app uses SQLite only (`shared_expenses.db`).
- Membership changes are tracked with join and optional leave dates.
- Use the settlement form to record payments between members.

## Assignment artifacts
- `README.md`: setup instructions and app notes
- `SCOPE.md`: CSV anomalies, data problems, and database schema
- `DECISIONS.md`: design and implementation decisions
- `AI_USAGE.md`: AI collaboration log and quality checks
- `IMPORT_REPORT.md`: CSV import anomaly report

## Deployment and repository status
- Public deployed URL: https://shared-expenses-app-jrs6.onrender.com
- Remote GitHub repository: https://github.com/Nitin-Sikarwar/Assignment
