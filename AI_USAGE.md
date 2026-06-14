# AI USAGE

## AI collaborator
- The app was built with the help of an AI assistant inside VS Code.
- The assistant helped write Python, Flask routes, templates, and the CSV import logic.

## Prompts used
- The main prompt was the assignment description: build a shared expenses app with login, groups, import, and split support.
- Additional prompts included requests for CSV parsing, duplicate detection, and data normalization.

## AI errors and corrections

1. Dependency version error
   - AI suggested `Flask==2.3.4` and `python-dateutil==2.8.4`.
   - `pip` could not install those exact versions.
   - Fix: updated to `Flask==2.3.3` and `python-dateutil==2.9.0`.

2. Import session serialization issue
   - AI code initially retained Python user objects inside the import preview session.
   - That would not serialize to JSON safely.
   - Fix: store plain Python dict data in the review session instead of model objects.

3. CSV settlement handling
   - The initial approach treated every row as an expense.
   - The assignment CSV includes a payment correction row (`Rohan paid Aisha back`).
   - Fix: detect single-person `split_with` rows with no `split_type` and record them as `Settlement` entries.

4. Bootstrap template cleanup
   - The AI inserted invalid or unnecessary CDN integrity attributes.
   - Fix: simplified the Bootstrap includes to valid working URLs.

## Summary
- The AI was a productive collaborator, but outputs were validated against actual `pip` installation behavior and runtime code review.
- Every mismatch was caught by running the app, checking installation, or reading generated code carefully.
