# 7-4 Pizza Toppings

# active = True
# while active:
#     topping = input("What kind of toppings do you like? ")
#     if topping.lower() in ["quit", "exit"]:
#         active = False
#     else:
#         print("OK, We will add " + topping.lower() + " on pizza.")


# topping = ""
# while topping.lower() not in ["quit", "exit"]:
#     topping = input("What kind of toppings do you like? ")
#     if topping.lower() not in ["quit", "exit"]:
#         print("OK, We will add " + topping.lower() + " on pizza.")


while True:
    topping = input("What kind of toppings do you like? ")
    if topping.lower() in ["quit", "exit"]:
        break
    else:
        print("OK, We will add " + topping.lower() + " on pizza.")

