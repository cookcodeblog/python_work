# 6-8 Pets

charlie = {
    'name': 'charlie',
    'kind': 'dog',
    'owner': 'John'
}

beta = {
    'name': 'beta',
    'kind': 'cat',
    'owner': 'Sunny'
}

gugu = {
    'name': 'gugu',
    'kind': 'fish',
    'owner': 'Jimmy'
}

pets = [charlie, beta, gugu]

for pet in pets:
    print(pet)

print()

for pet in pets:
    print(pet['name'].title() + " is a " + pet['kind'].lower() + ", and its owner is " + pet['owner'].title() + ".\n")
