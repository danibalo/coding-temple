# Product Finder

## Objective

This project uses Python and SQLite to query a small electronics-store product database. It demonstrates filtering, searching, sorting, and limiting SQL query results.


## Project File

- `product_finder.py` — creates the database, inserts sample products, and runs the five SQL queries.

## Technologies

- Python
- SQLite
- Python `sqlite3` module

## Database Structure

The `products` table contains the following columns:

| Column | Data type | Description |
|---|---|---|
| `id` | `INTEGER` | Primary key with autoincrement |
| `name` | `TEXT` | Product name |
| `category` | `TEXT` | Product category |
| `price` | `REAL` | Product price |
| `rating` | `REAL` | Customer rating |
| `in_stock` | `INTEGER` | Stock status: `1` for in stock and `0` for out of stock |

## Queries

The program answers the following questions:

1. Which products are out of stock?
2. Which products have a rating of `4.5` or higher and cost less than `$100`?
3. What are the three most expensive products in the `Accessories` category?
4. Which products have `Monitor` in their name?
5. Which products are not in the `Accessories` category and are currently in stock?

## SQL Concepts Demonstrated

- `SELECT`
- `WHERE`
- `AND`
- `LIKE`
- `ORDER BY`
- `LIMIT`
- Comparison operators
- Parameterized data insertion with `executemany()`

## Running the Program

Run the following command from the project directory:

```bash
python product_finder.py
```

## Example Output

```text
====== OUT-OF-STOCK PRODUCTS ======
Name: USB-C Hub | Category: Accessories
Name: Bluetooth Speaker | Category: Audio

====== 3 MOST EXPENSIVE ACCESSORIES ======
Name: Mechanical Keyboard | Price: $89.99
Name: Webcam HD | Price: $49.99
Name: Laptop Stand | Price: $39.99
```

## Note

The project uses an in-memory SQLite database:

```python
sqlite3.connect(":memory:")
```

The database exists only while the program is running. All stored data is removed when the database connection closes.