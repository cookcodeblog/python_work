# 7-5 Buy Ticket.

age = input("How old are you? ")

price = 0
if 3 <= int(age) <= 12:
    price = 10
elif int(age) > 12:
    price = 15

if price > 0:
    print("You need pay $" + str(price))
else:
    print("You are free.")