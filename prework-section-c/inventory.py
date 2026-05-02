#!/usr/bin/env python3
inventory = {
        "shampoo" : {"price": 25.99, "quantity": 2}, 
        "eye glass" : {"price": 345.25, "quantity":3}, 
        "jacket" : {"price":34.25, "quantity": 25}, 
        "shoes":{"price":34.45, "quantity":14}
        }
print("=" * 50)
print(" " * 15, "DISPLAY THE INVENTORY")
print("=" * 50)

#display_inventory() shows the inventory in table format, whith item name, quantity, product value, and the inventroy's is total

#product value is calculated by multiplying the quantity by price
#the total value of the inventory is the some of each product's value 
def display_inventory():
    total_value = 0
    print(f"{'Item':<12}{'Price':<12}{'Quantity':<12}{'Product Value':<12}\n")
    for key, values in inventory.items():
        product_value = values['price'] * values['quantity']
        print(f"{key:<12} {values['price']:<12.2f} {values['quantity']:<12} {product_value:<12.2f}")
        total_value += product_value
    print("-"*50)
    print(f"Total: {total_value:39.2f}")
display_inventory()
print()

#product_lookup()
#THIS allows a user to search the product they want. If the product is in inventory it shows them the price and quantity
#if they search other thing it tells them the product is not available
def product_lookup():
    search = input("Enter your product: ").lower()
    product = inventory.get(search)
    if product:
        print(f"Your search is found... {search}") 
        print(f"The price is: {product['price']} and there are {product['quantity']} quantity available")
    else:
        print(f"This product is not available")
#update_quantity() updates the quantity off the product they want. They can add the quantity or minimize quantity
#if they enter the product that is not available the program tells them the product is not avialable
def update_quantity():
    product1 = input('Enter the product you want to update their quantity: ').lower()
    update  = inventory.get(product1)
    if update:
        print(f"If you want add  quantity of {product1}, type 1, If you want to decrease type , 2")
        #they will have an option of adding quantity of product or minimizing quantity of product
        #if they put another character either one or two?, the program exits
        choice = input("enter your choice: ")
        if choice == "1":
            add = int(input("how many you want to add?: "))
            update["quantity"] += add
            inventory[product1] = update
            print(f"you successfully added in to inventory, now the quantity of your {product1} is: {update['quantity']} ")
            display_inventory()
        
        elif choice == "2":
            sub = int(input("how many product you want to take out?: "))
            update["quantity"] -= sub
            if (update["quantity"]) < 0:
                print("Sorry, we don't have this much amount of this quantity in inventory, please enter less")
                exit()
            else:
                inventory[product1] = update
                print(f"You successfully minimized  your inventory, your quantity of {product1} is: {update['quantity']}")
                display_inventory()
        else:
            print(f"Wrong Choice... exititing...")
            exit()
    else: 
        print(f"no {product1} in the inventory")
product_lookup()
update_quantity()
#A function which tracks low quantity in inventory, it shows them if they are less than 10 in quantity
def show_stock():
    stock = set()
    for key, values in inventory.items():
        if values['quantity'] < 10:
            stock.add(key)
    print("="* 40)
    print(" CITY STOCK")
    print("-" * 40)
    print(f"These items are low in stock, less than 10 available in inventory {stock}")
show_stock()




