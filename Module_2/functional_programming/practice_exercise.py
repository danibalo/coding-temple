from functools import reduce
#dictionary of products
products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]
#FILTER
#1. First method
stock_first = [p for p in products if p["in_stock"]]
#print(stock_first)
#2.Second Method
stock = list(filter(lambda p:p['in_stock'], products))
#MAP
def discounted(product):
    return {**product, "discounted_price":product["price"] * 0.9}
discount = list(map(discounted, products))
#3.Filter
electronics = [p for p in products  if p['category'] == 'electronics' and p['price'] < 200]
#OR
electronics = list(filter(lambda p:p['category'] == 'electronics' and p['price'] < 200, products))
#print(electronics)
#4. SORTING
sorted_products = sorted(products, key=lambda p:p['price'])
#print(sorted)
#   REDUCE
total =  reduce(lambda acc, p: acc + p['price'], stock, 0)
#Or
total_2 = sum(p['price'] for p in stock)
#Group broducts
categories = {product['category'] for product in products}
grouped = {
    category: [product['name'] for product in products if product['category'] == category] for category in categories
}
print(grouped)
