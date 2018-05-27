# 3-1 Names
# Store some friends' names in a list, and name the list as "names"
# And then travel the list, and print each friend's name

names = ["Dog", "Cat", "Rabbit", "Duck"]
print(names)
print()

# from beginning to ending
print(names[0] + ", " + names[1] + ", " + names[2] + ", " + names[3])
print()

# from ending to beginning
print(names[-4] + ", " + names[-3] + ", " + names[-2] + ", " + names[-1])
print()

# print in a loop
for name in names:
    print(name)
