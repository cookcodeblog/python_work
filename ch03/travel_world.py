# 3-8 Travel the World
# Write some places you want to travel
# Store them in a list with random sequence

places = ["London", "Paris", "Washington", "Tokyo", "Berlin"]

print(places)

print()

# Print list in sort
print(sorted(places))

print()

# Print the list again to prove the lis not changed
print(places)

print()

# Print list in reversed sort
print(sorted(places, reverse=True))

print()

# Print the list again to prove the lis not changed
print(places)

print()

places.reverse()
print(places)

places.reverse()
print(places)


places.sort()
print(places)

places.sort(reverse=True)
print(places)

print("How many places you want to travel: " + str(len(places)))
