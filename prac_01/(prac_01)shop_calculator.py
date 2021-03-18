"""
CP1404/CP5632 - Practical
Program that processes and displays the prices and quantities
of items, and determines discounts if applicable
"""
price_total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    price_total += item_price
if price_total > 100:
    discount = price_total * 0.1
    price_total = price_total - discount
print(f"Total price for {number_of_items} items is ${price_total:.2f}")
