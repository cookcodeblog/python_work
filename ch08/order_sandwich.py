# 8-12 Order Sandwich


def order_sandwich(*toppings):
    """One star means accept tuple parameter (each item is a parameter)"""
    print("Start to make your sandwich...")
    for topping in toppings:
        print("Adding " + topping)
    print("Your sandwich were made.\n")


order_sandwich("Egg")
order_sandwich("Chimp", "Beef")
order_sandwich("Onion", "Cheers", "Sauce")
