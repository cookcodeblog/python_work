from ch09.restaurant import Restaurant
from ch09.restaurant import IceCreamStand

food_time = Restaurant('Food Time', 'Chinese')
food_time.open_restaurant()
food_time.describe_restaurant()

print()

kfc = Restaurant("KFC", "Western Fast Food")
kfc.describe_restaurant()
print()

pizza_hub = Restaurant("Pizza Hub", "Pizza")
pizza_hub.describe_restaurant()
print()

haidilao = Restaurant("Hai Di Lao", "Sichuan Hotpot")
haidilao.describe_restaurant()
print()

dongbeiren = Restaurant("Dong Bei Ren", "Dongbei", 1234)
dongbeiren.describe_restaurant()
dongbeiren.set_number_served(1240)
dongbeiren.describe_restaurant()
dongbeiren.increment_number_served(50)
dongbeiren.describe_restaurant()

# IceCream
print()

turkey_ice_cream = IceCreamStand("Turkey Ice Cream", "Turkey", ["Sweet", "Sea", "Weird", "Coconut", "Fruit"], 0)
turkey_ice_cream.describe_restaurant()
turkey_ice_cream.describe_ice_cream()
turkey_ice_cream.increment_number_served(190)
turkey_ice_cream.describe_restaurant()
