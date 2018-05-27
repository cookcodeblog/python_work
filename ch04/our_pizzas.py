# 4-11 Your Pizzas and My Pizzas

my_pizzas = ["Beef Pizza", "Classic Pizza", "Hawaii Pizza"]
your_pizzas = my_pizzas[:]

print("My pizzas are " + str(my_pizzas))
print("Your pizzas are " + str(your_pizzas))

my_pizzas.append("Thin Pizza")
your_pizzas.append("Thick Pizza")

print("My pizzas are " + str(my_pizzas))
print("Your pizzas are " + str(your_pizzas))


print()

for pizza in my_pizzas:
    print("I lik " + pizza)

print()

for pizza in your_pizzas:
    print("You like " + pizza)

