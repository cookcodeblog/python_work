# 7-8 Sandwich

sandwich_orders = ["Tuna", "Beef", "Chicken", "Pastrami", "Egg", "Pastrami", "Onion", "Pastrami"]

print(sandwich_orders)

# Remove all "Pastrami" from order list
print("Pastrami is sell out.")
while "Pastrami" in sandwich_orders:  # Must use "item in list" syntax, otherwise will have a remove error
    sandwich_orders.remove("Pastrami")  # Call remove once, only remove one item; have to use while loop to remove all
print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(finished_sandwich)
    print("I made your " + finished_sandwich.lower() + " sandwich.")

print("\nAdd sandwich are made:")
for sandwich in finished_sandwiches:
    print(sandwich)
