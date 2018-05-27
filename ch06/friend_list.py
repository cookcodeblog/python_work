# 6-7 Friend List

friend_william = {
    'first_name': 'William',
    'last_name': 'Lin',
    'age': 32
}

friend_tome = {
    'first_name': 'Tome',
    'last_name': 'He',
    'age': 34
}

friends = [friend_william, friend_tome]

for friend in friends:
    print(friend)

print()

for friend in friends:
    print(friend['first_name'].title() + " " + friend['last_name'].title() +
          " is " + str(friend['age']) + " years old.")
