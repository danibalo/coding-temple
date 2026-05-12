#!/usr/env/python
import csv
sales = []
#function to calculate a total of list:
def calculate_total(lst):
    total = 0
    for member in lst:
        total += member
    return total
with open('sales_data.csv', 'r') as file:
          reader = csv.DictReader(file)
          for row in reader:
              row['quantity'] = int(row['quantity'])
              row['price'] = float(row['price'])
              sales.append(row)
print(sales)
#calculates total revenue
print("\n === Total revenue ===")
total_revenue = 0
for sale in sales:
    total_revenue += sale['quantity'] * sale['price']
print(f"Total Revenue: {total_revenue:.2f}")

#revenue per product
revenue_per_product = {}
for sale in sales:
    product = sale['product']
    if product not in revenue_per_product:
        revenue_per_product[product] = []
    revenue_per_product[product].append(round(sale['quantity'] * sale['price'], 2))

print("= = = REVENUE PER PRODUCT = = =")
for product,revenue in revenue_per_product.items():
    print(f"{product} total revenue is :{calculate_total(revenue)}")

#Quantity per product
quantity_per_product = {}
for sale in sales:
    product = sale['product']
    if product not in quantity_per_product:
        quantity_per_product[product] = []
    quantity_per_product[product].append(sale['quantity'])
print("=== quantity per product ===")
for product, quantity in quantity_per_product.items():
    print(f"A total of {calculate_total(quantity)} {product} is sold")

#revenue per day.
print("=== Day with highest total revenue ===")
revenue_per_day = {}
for sale in sales:
    date = sale['date']
    if date not in revenue_per_day:
        revenue_per_day[date] = []
    revenue_per_day[date].append(sale['quantity'] * sale['price'])
def get_total(day):
    return calculate_total(revenue_per_day[day])
max_day = max(revenue_per_day, key=get_total)
print(f"highest day is {max_day} with revenue of {get_total(max_day)}")
#Write a result to a text file:
with open("sales_report.txt", "w") as file:
    file.write("Sales Report\n")
    file.write('=' * 45)
    file.write(f"\nTotal Revenue: {total_revenue}")
    file.write("\n= = = Revenue per product = = =\n")
    for product, revenue in revenue_per_product.items():
        file.write(f"{product} total revenue is: {sum(revenue)}\n")
    file.write("= = = Quantity per product = = =\n")
    for product, quantity in quantity_per_product.items():
        file.write(f"A total of {sum(quantity)} {product} is sold\n")
    file.write(f"highest day is {max_day} with revenue of {get_total(max_day)}")
print("the result is written to 'sales_report.txt' file ")

#writing summary to csv file
with open("product_summary.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['product', 'total_quantity', 'total_revenue'])
    writer.writeheader()
    for product in revenue_per_product:
        writer.writerow({
            'product': product,
            'total_quantity':sum(quantity_per_product[product]),
            'total_revenue': round(sum(revenue_per_product[product]), 2)
            })
print("the summary is written to csv file with columns product, total_quantity, total_revenue")
