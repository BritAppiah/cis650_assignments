#Create a script that will
# prompt the user for number of items,
# then ask for item name, and item price for each item
# Then it will print the items, prices, number of items, and total price
# Make the output easy to read on the terminal.
# Do not use any data structures or any package for display
items_count = 0
total_price = 0.0
items_output = ""
seperator = "-" * 40
print("Welcome to the Grocery Bill Calculator")
print(seperator)   
num_items = int(input("Enter the number of items: "))

while items_count < num_items:
    items_count += 1
    item_name = input(f"Enter the name of item {items_count}: ")
    item_price = float(input(f"Enter the price of {item_name}: $"))
    total_price += item_price

    items_output += f"{items_count}. {item_name}: ${item_price:.2f}\n"

print(seperator)
print("Grocery Bill Summary")
print(seperator)
print(items_output)
print(seperator)
print(f"Total number of items: {items_count}")
print(f"Total price: ${total_price:.2f}")
print(seperator)
print("Thank you for using the Grocery Bill Calculator!")




#git commit -m 'updated 05_grocery_bill' and then
#git push
