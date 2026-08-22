import sqlite3
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

#members table
cursor.execute(

    """CREATE TABLE IF NOT EXISTS members (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
join_date TEXT)
""")
#books table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    year_published INTEGER
    )
"""
)
#checkouts table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS checkouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER,
    book_id INTEGER,
    checkout_date DATE NOT NULL,
    return_date DATE,
        FOREIGN KEY(member_id) REFERENCES members(id),
          FOREIGN KEY(book_id) REFERENCES books(id))
    """)
members = [
    ('Daniel Krosty', '2024-02-08'),
    ('James Red', '2025-01-11'),
    ('Alard Rice', '2021-04-02'),
    ('Vine Dray', '2022-08-02'),
    ('Ede Vohel', '2023-06-02')
]
cursor.executemany(
    "INSERT INTO members(name, join_date) VALUES(?,?)", (members),
)

books = [
("The Hobbit","Fantasy",1937),
("Dune","Science Fiction", 1965),
("The Murder of Roger Ackroyd","Mystery",1926),
("Pride and Prejudice","Romance",1813),
("The Haunting of Hill House", "Horror",1959),
("The Book Thief","Fiction", 2005),
("I Know Why the Caged Bird Sings", "Memoir", 1969),
("One Hundred Years of Solitude","Horror", 1967)
]
cursor.executemany(
    "INSERT INTO books(title, genre, year_published) VALUES (?,?,?)", (books)
)
checkouts = [
     (3, 1, "2021-05-10", "2021-05-24"),(3, 4, "2021-08-03", "2021-08-18"),
     (3, 6, "2022-01-12", "2022-01-29"), (4, 2, "2022-09-05", "2022-09-20"),
    (4, 5, "2023-01-14", "2023-02-02"), (5, 3, "2023-07-08", "2023-07-21"),
    (5, 7, "2023-10-11", "2023-10-30"), (1, 1, "2024-02-15", "2024-03-01"),
    (1, 8, "2024-04-06", "2024-04-25"), (3, 2, "2024-05-10", "2024-05-28"),
    (4, 4, "2024-07-02", "2024-07-19"), (5, 6, "2024-09-13", "2024-10-01"),
    (1, 5, "2024-11-04", "2024-11-22"), (2, 3, "2025-01-15", "2025-02-03"),
    (2, 7, "2025-03-08", "2025-03-26"), (3, 8, "2025-05-17", "2025-06-02"),
    (4, 1, "2025-07-09", "2025-07-25"), (5, 2, "2025-09-14", "2025-10-03"),
    (1, 6, "2026-07-20", None), (2, 4, "2026-08-05", None)
    ]

cursor.executemany("INSERT INTO checkouts(member_id, book_id, checkout_date, return_date) VALUES(?,?,?,?)", (checkouts))
#QUERY 1
#How many books are in each genre?
cursor.execute(
    """SELECT count(*) AS book_count, b.genre
FROM books b
GROUP BY genre
""")
print("Books in each genre:")
for row in cursor.fetchall():
    print(f"{row[1]} - {row[0]}")
#QUERY 2
#Which member has checked out the most books?
cursor.execute("""
    SELECT m.name, COUNT(c.checkout_date) AS checkout_count
    FROM members AS m
    JOIN checkouts AS c
        ON c.member_id = m.id
    GROUP BY m.id, m.name
    ORDER BY checkout_count DESC
    LIMIT 1
""")
print("Member who checked out Most books:")
for row in cursor.fetchall():
    print(f"{row[0]} has checked out {row[1]} books")
# What is the average number of checkouts per member?
cursor.execute(
    """ SELECT AVG(count_per)
    FROM (SELECT member_id, count(*) as count_per
    FROM checkouts c
    GROUP BY member_id)
    
"""
)
print("Average number of checkouts per member")
for row in cursor.fetchall():
    print(row)
#Which genres have more than 3 checkouts?
cursor.execute(
    """ SELECT b.genre, count(c.id) as genre_count
    FROM  checkouts c
    LEFT JOIN books b  on  b.id = c.book_id
    GROUP BY b.genre
    HAVING count(c.id) > 3
"""
)
print("A Genre that has more than 3 checkouts: ")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")
#Which books have never been checked out? 
cursor.execute(
    """ SELECT *
    FROM books
    WHERE id NOT IN (SELECT book_id
    FROM checkouts)
 
"""
)

print("A book that has never been checked out:")
rows = cursor.fetchall()

if not rows:
    print("Every book has been checked out at least once.")
else:
    print("Books that have never been checked out:")
    for book_id, title in rows:
        print(f"{book_id} - {title}")