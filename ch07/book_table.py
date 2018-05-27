# Book Table

people_count = input("How many sits do you need ? ")
if int(people_count) > 8:
    print("Sorry, we don't have more than 8 sits table.")
else:
    print("OK, I will book a " + people_count + " sits table for you.")
