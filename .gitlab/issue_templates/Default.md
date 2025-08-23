# Default Issue Template

**Summary:**
The "Search Function" on the platform returns incomplete results when filtering by date.

**Steps to Reproduce / Context:**
1. Go to the dashboard.
2. Enter a keyword in the search bar (e.g., "invoice").
3. Apply a date filter (e.g., "Last 7 Days").
4. Notice that only partial results are displayed instead of all matching entries.

**Expected Behavior / Outcome:**
All invoices from the last 7 days that match the keyword should appear in the results.

**Actual Behavior (if applicable):**
Only 2–3 invoices appear, while several others within the date range are missing.

**Proposed Solution (if applicable):**
- Review backend query logic for date filters.
- Ensure proper indexing on the "created_at" field in the database.
- Add automated test cases for date-filtered searches.

**Additional Context:**
- Issue reported by multiple QA testers.
- Related ticket: #145 (Search Bar Bug).
