## Library Analytics Practice Problem

**Objective:** Use aggregations and subqueries to answer questions about a library database.

### IT Does

1. Create a Python file named `library_analytics.py`.

2. Build an in-memory SQLite database with three tables:

   - `members`: `id`, `name`, `join_date`
   - `books`: `id`, `title`, `genre`, `year_published`
   - `checkouts`: `id`, `member_id`, `book_id`, `checkout_date`, `return_date`

   The `return_date` can be `NULL` if the book has not been returned.

3. Insert sample data containing:

   - At least 5 members
   - At least 8 books across 3 or more genres
   - At least 15 checkouts

4. Write SQL queries to answer the following questions:

   - How many books are in each genre? (`GROUP BY`)
   - Which member has checked out the most books? (`GROUP BY`, `ORDER BY`, and `LIMIT`)
   - What is the average number of checkouts per member? (Subquery or nested aggregation)
   - Which genres have more than 3 checkouts? (`GROUP BY` and `HAVING`)
   - Which books have never been checked out? (Subquery with `NOT IN`)