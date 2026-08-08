# Practice Proplem
## The data:
*** products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]
***
## Uses list comprehensions, map, filter, and/or lambda:
- Get all in-stock products (filter)
- Add a "discounted_price" field that’s 10% off the original (map - create new dicts, don’t mutate)
-Get only electronics under $200 (filter with two conditions)
-Sort all products by price, lowest first (use sorted with a key lambda)
-Calculate the total value of all in-stock products (reduce or sum with comprehension)
-Group products by category, return a dictionary like {"electronics": [...], "books": [...], ...}
*** Do not use for loops with append. Use comprehensions or functional tools only. Do not modify the original products list.***