# 7-10 Visit Poll

visit_places = {}
poll_active = True
while poll_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    visit_places[name] = place  # It is like map.put(key, value)
    repeat = input("Would you like to let another person respond? (yes / no)")
    if repeat.lower() == "no":
        poll_active = False

print("\n---Poll Result---\n")
for name, place in visit_places.items():
    print(name.title() + " likes to visie " + place.title() + ".")
