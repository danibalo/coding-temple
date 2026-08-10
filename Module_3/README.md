# Music Database Practice Problem

## Overview

This project uses **Python** and **SQLite** to create a simple music collection database.

The program creates two related tables, inserts sample artists and albums, and uses a SQL `JOIN` to display each album with its artist.

---

## Project Files

```text
music_db.py
music.db
README.md
```

- `music_db.py` contains the Python program.
- `music.db` is the SQLite database created by the program.
- `README.md` contains the project documentation.

---

## Database Structure

### Artists Table

| Column | Type | Description |
| --- | --- | --- |
| `id` | INTEGER | Primary key with autoincrement |
| `name` | TEXT | Artist name; cannot be empty |
| `genre` | TEXT | Artist's music genre |

### Albums Table

| Column | Type | Description |
| --- | --- | --- |
| `id` | INTEGER | Primary key with autoincrement |
| `title` | TEXT | Album title; cannot be empty |
| `year` | INTEGER | Album release year |
| `artist_id` | INTEGER | Foreign key referencing `artists(id)` |

Each artist can have multiple albums, while each album belongs to one artist.

---

## Sample Data

### Artists

- Michael Jackson — Pop
- Justin Bieber — R&B
- Rihanna — Reggae

### Albums

- *BEN* — Michael Jackson, 1972
- *Changes* — Justin Bieber, 2020
- *Music of the Sun* — Rihanna, 2005
- *Music and Me* — Michael Jackson, 1973
- *Rated R* — Rihanna, 2009

---

## Program Features

The `music_db.py` program:

1. Connects to a SQLite database named `music.db`.
2. Enables SQLite foreign-key enforcement.
3. Creates the `artists` and `albums` tables.
4. Inserts three artists and five albums.
5. Uses a `JOIN` to connect albums to their artists.
6. Orders the results by artist name and album year.
7. Prints the results.
8. Closes the database connection.

---

## Requirements

- Python 3
- Python's built-in `sqlite3` module

No external packages are required.

---

## How to Run

Open a terminal in the project folder and run:

```bash
python music_db.py
```

If your system uses `python3`, run:

```bash
python3 music_db.py
```

The program creates `music.db` automatically if it does not already exist.

---

## Expected Output

```text
Albums by artist:
  Justin Bieber — Changes (2020)
  Michael Jackson — BEN (1972)
  Michael Jackson — Music and Me (1973)
  Rihanna — Music of the Sun (2005)
  Rihanna — Rated R (2009)
```

---

## Foreign-Key Enforcement

SQLite does not enforce foreign keys by default. The program enables them with:

```python
connection.execute("PRAGMA foreign_keys = ON")
```

The `albums` table references the `artists` table using:

```sql
FOREIGN KEY (artist_id) REFERENCES artists(id)
```

---

## Author

**Daniel T**