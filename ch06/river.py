# 6-5 River

rivers = {
    'Nile': 'Egypt',
    'Changjiang': 'China',
    'Ganges River': 'India'
}

for river, location in rivers.items():
    print("The " + river + " runs through " + location + ".\n")

for river in rivers.keys():
    print(river)


print()

for location in rivers.values():
    print(location)
