import sqlite3
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
#Create a product table
cursor.execute(
    """ CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    rating REAL,
    in_stock INTEGER DEFAULT 1
)
"""
)
#INSERT A SAMPLE DATA FROM SMALL ELECTRONICS STORE
products = [
    ("Wireless Mouse", "Accessories", 29.99, 4.5, 1),
    ("Mechanical Keyboard", "Accessories", 89.99, 4.8, 1),
    ("USB-C Hub", "Accessories", 34.99, 4.2, 0),
    ("27-inch Monitor", "Displays", 299.99, 4.6, 1),
    ("24-inch Monitor", "Displays", 179.99, 4.3, 1),
    ("Webcam HD", "Accessories", 49.99, 3.9, 1),
    ("Noise-Canceling Headphones", "Audio", 199.99, 4.7, 1),
    ("Bluetooth Speaker", "Audio", 59.99, 4.1, 0),
    ("Laptop Stand", "Accessories", 39.99, 4.4, 1),
    ("External SSD 1TB", "Storage", 89.99, 4.6, 1),
    ("External SSD 2TB", "Storage", 149.99, 4.5, 1),
    ("Flash Drive 64GB", "Storage", 12.99, 4.0, 1),
]
cursor.executemany (
    "INSERT INTO products(name, category, price, rating, in_stock) VALUES(?,?,?,?,?)" , (products),)
connection.commit()
#1. products that are out of stock
print("\n====== OUT OF STOCK PRODUCTS======")
cursor.execute(
    """ SELECT name,category
    FROM products
    WHERE in_stock = 0

"""
)
for row in cursor.fetchall():
    print(f"Name: {row[0]} Category: {row[1]}")
#2 products that are rated 4.5 or higher that costs less than 100
print("\n===== Rating 4.5 + and price < 100 $=======")
cursor.execute(
    """
SELECT name, rating, price
FROM products
WHERE rating >= 4.5 AND
price < 100
"""
)
for row in cursor.fetchall():
    print(f"Name: {row[0]} | Rating: {row[1]} | Price: {row[2]}")
#3 Three most expensive Accessories
print("\n====== 3 Most Expensive Accessory products=============== ")
cursor.execute (
    """ SELECT name, price
    FROM products
    WHERE category = 'Accessories'
    ORDER BY price DESC
    LIMIT 3
"""
)
for row in cursor.fetchall():
    print(f"Name: {row[0]} - Price: {row[1]}")
#4 Which products have "Monitor" in their name? Show all columns
cursor.execute(
    """SELECT * 
    FROM products
    WHERE name LIKE '%Monitor%'
""")
for row in cursor.fetchall():
    print(f"ID: {row[0]} Name: {row[1]} Category: {row[2]} Price: {row[3]} Rating: {row[4]} In Stock: {row[5]}")
#5 Which products are not in the "Accessories" category and are in stock? 
#show name, category, price sorted by category then price
print("\n========= NOT in Accessories =======")
cursor.execute(
    """ SELECT name, category, price
    FROM products
    WHERE category NOT IN  ('Accessories')
    AND in_stock = 1
    ORDER BY category, price
"""
)
for row in cursor.fetchall():
    print(f"Name: {row[0]}  Category: {row[1]} Price: {row[2]}")