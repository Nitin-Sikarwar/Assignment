# DECISIONS

## Technology stack
- Chose Flask + SQLite for the app.
- Reason: lightweight, easy to run locally, meets the relational DB requirement, and allows quick prototyping.
- Alternative: a full React + API stack, but that would be overkill for the assignment scope.

## Login module
- Implemented basic username/password authentication.
- Option considered: OAuth or third-party login.
- Chose simple local auth because it satisfies the requirement without adding external dependencies.

## Group and membership model
- Designed `GroupMember` with `joined_at` and optional `left_at`.
- This supports membership changes over time and allows computing balance based on active membership.
- Alternative: flat user lists per expense, but this would not handle member transitions cleanly.

## Expense import and anomaly handling
- Built a CSV import review step instead of blindly importing every row.
- User can review and approve or skip rows, which aligns with Meera's request for approval before automatic cleanup.
- Alternative: auto-clean everything silently, but that is unsafe with messy data.

## Currency handling
- Converted USD to INR using a fixed rate (`USD_TO_INR_RATE = 83.0`).
- This satisfies Priya's request to treat currencies correctly instead of pretending USD = INR.
- Alternative: live FX rates were not used because the assignment focuses on CSV cleanup, not a real exchange rates integration.

## Split type support
- Supported `equal`, `percentage`, `unequal`, `share`, and settlement rows.
- For rows with no `split_type` and a single split target, the row is treated as a settlement.
- This was necessary because the CSV includes both expense entries and payment corrections.

## Duplicate detection
- Normalized candidate keys by date, description, payer, amount, currency, split type, and participant list.
- Duplicate rows are flagged as candidates, but the user retains final choice on import.
- This avoids accidentally deleting ambiguities without approval.

## Deployment and repo status
- No public deployed URL is currently available from this local workspace.
- The local git repository is initialized for commit history, but no remote GitHub repository has been set.
