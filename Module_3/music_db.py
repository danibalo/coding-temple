"""

Connect to a SQLite database, create two related tables, insert sample
artists and albums, and query across the tables using a JOIN.
"""

import sqlite3


# ── Database setup ────────────────────────────────────────────────────────────

# Connect to music.db. SQLite creates the file if it does not already exist.

connection = sqlite3.connect("music.db")

# Foreign-key enforcement must be enabled explicitly in SQLite.

connection.execute("PRAGMA foreign_keys = ON")

# This allows columns to be accessed by name, such as row["title"].

connection.row_factory = sqlite3.Row


# ── Create tables ─────────────────────────────────────────────────────────────

def create_tables(connection: sqlite3.Connection) -> None:
    """
    Create the artists and albums tables.

    Schema:
      artists: id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               genre TEXT

      albums:  id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               year INTEGER,
               artist_id INTEGER (FK -> artists.id)
    """

    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            genre TEXT
        );

        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        );
        """
    )


# ── Insert data ───────────────────────────────────────────────────────────────

def insert_data(connection: sqlite3.Connection) -> None:
    """
    Insert three artists and five albums into the database.

    Michael Jackson and Rihanna each have multiple albums.
    """

    artists = [
        ("Michael Jackson", "Pop"),
        ("Justin Bieber", "R&B"),
        ("Rihanna", "Reggae"),
    ]

    # Insert each artist and save the generated artist ID.

    artist_ids = {}

    for name, genre in artists:
        cursor = connection.execute(
            "INSERT INTO artists (name, genre) VALUES (?, ?)",
            (name, genre),
        )
        artist_ids[name] = cursor.lastrowid

    albums = [
        ("BEN", 1972, artist_ids["Michael Jackson"]),
        ("Changes", 2020, artist_ids["Justin Bieber"]),
        ("Music of the Sun", 2005, artist_ids["Rihanna"]),
        ("Music and Me", 1973, artist_ids["Michael Jackson"]),
        ("Rated R", 2009, artist_ids["Rihanna"]),
    ]

    connection.executemany(
        """
        INSERT INTO albums (title, year, artist_id)
        VALUES (?, ?, ?)
        """,
        albums,
    )

    connection.commit()


# ── Query albums ──────────────────────────────────────────────────────────────

def query_albums(connection: sqlite3.Connection) -> list:
    """
    Return all albums with their artist names.

    Each row includes the album title, release year, and artist name.
    Results are ordered by artist name and release year.
    """

    cursor = connection.execute(
        """
        SELECT
            albums.title,
            albums.year,
            artists.name
        FROM albums
        JOIN artists
            ON albums.artist_id = artists.id
        ORDER BY artists.name, albums.year
        """
    )

    return cursor.fetchall()


# ── Main program ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        create_tables(connection)
        insert_data(connection)

        results = query_albums(connection)

        print("Albums by artist:")

        for row in results:
            print(f"  {row['name']} — {row['title']} ({row['year']})")
    finally:
        connection.close()


# Expected output:
# Albums by artist:
#   Justin Bieber — Changes (2020)
#   Michael Jackson — BEN (1972)
#   Michael Jackson — Music and Me (1973)
#   Rihanna — Music of the Sun (2005)
#   Rihanna — Rated R (2009)