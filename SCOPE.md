# SCOPE

## Data anomalies found in `Expenses Export.csv`

1. Inconsistent date formats
   - Standard `DD-MM-YYYY` but also `Mar-14` and ambiguous `04-05-2026`.
   - Fixed by using a tolerant parser with day-first normalization.

2. Duplicate entries
   - `Dinner at Marina Bites` appears twice with identical date, payer, and amount.
   - Detected as duplicate candidates in import review for manual approval.

3. Missing or invalid payer
   - `House cleaning supplies` has no `paid_by` value.
   - The importer flags these rows for review and does not automatically assign a payer.

4. Missing currency
   - `Groceries DMart` on 15-03-2026 has a blank currency.
   - Defaulted to `INR` during import.

5. USD entries, trip expenses, and currency handling
   - `Goa villa booking`, `Beach shack lunch`, `Parasailing`, and a refund are in `USD`.
   - Converted to INR with a fixed exchange rate in the imported balance calculations.

6. Settlement row misclassified as expense
   - `Rohan paid Aisha back` has empty `split_type` and a single `split_with` participant.
   - Identified as a settlement and recorded as a payment, not an expense.

7. Split type inconsistencies
   - `percentage` row totals do not sum to exactly 100%.
   - `share` rows are labeled `equal` but contain explicit per-person shares.
   - The importer normalizes these cases and reports parser warnings.

8. Zero-amount row
   - `Dinner order Swiggy` has amount `0`, indicating a likely correction entry.
   - The importer preserves it for review but does not include it as a normal expense.

9. Name normalization
   - Names appear in multiple forms: `priya`, `Priya S`, `rohan `, `Dev`.
   - The app normalizes names to title case and trims whitespace.

## Database schema summary

- `User`
  - `id`, `username`, `email`, `password_hash`, `joined_at`

- `Group`
  - `id`, `name`, `owner_id`, `created_at`

- `GroupMember`
  - `id`, `group_id`, `user_id`, `joined_at`, `left_at`
  - Tracks membership periods for join/leave history.

- `Expense`
  - `id`, `group_id`, `created_by_id`, `date`, `description`, `paid_by_user_id`, `raw_amount`, `currency`, `amount_in_base`, `split_type`, `split_details`, `notes`, `created_at`

- `ExpenseShare`
  - `id`, `expense_id`, `user_id`, `amount`, `share_description`
  - Records per-person share amounts after normalization.

- `Settlement`
  - `id`, `group_id`, `from_user_id`, `to_user_id`, `amount`, `currency`, `date`, `notes`, `created_at`
  - Captures payments between users separate from expense splits.
