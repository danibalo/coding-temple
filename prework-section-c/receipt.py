#Definig variables as strings, these are datas that came from a file or form

#data for first item
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"
#convert this data to appropriate types for calculation
item1_price = float(item1_price)
item1_qty = int(item1_qty)


#data for seond item
item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

#converting th second item datas to appropriate data type for calculation
item2_price = float(item2_price)
item2_qty = int(item2_qty)

#data for third item
item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"
#converting the third item data to appropriate data type for calculation
item3_price = float(item3_price)
item3_qty = int(item3_qty)

tax_rate = "0.075" #7.5 % sales tax
#tax rate with appropriate data type
tax_rate = float(0.075)
#first item total, calculated by multpliyng the unit price by quantity
item1_total = item1_price * item1_qty
#second item total, calculated by multpliyng the unit price by quantity
item2_total = item2_price * item2_qty
#third item total, calculated by multpliyng the unit price by quantity
item3_total = item3_price * item3_qty
#sub total is the additon of all total items
subtotal = item1_total + item2_total + item3_total
#tax is calculated by subtotal multiplied by tax rate
tax = subtotal * tax_rate
#grand total is subtotal plus tax
grand_total = subtotal + tax
print('=' * 40,'\n', ' ' * 10, ' STORE RECEIPT\n','=' * 40)
print(f"Notebook: ${item1_price:.2f} x {item1_qty}      ${item1_total:.2f}")
print(f"Pen Pack: ${item2_price:.2f} x {item2_qty}      ${item2_total:.2f}")
print(f"Backpack: ${item3_price:.2f} x {item3_qty}      ${item3_total:.2f}")
print('-' * 40)
print(f"Subtotal:               ${subtotal:.2f}")
print(f"Tax(7.5%):              ${tax:.2f}")
print('=' * 40)
print(f"TOTAL:                  ${grand_total:.2f}")
print('=' * 40)