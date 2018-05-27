# 6-2 Lucky Number

lucky_numbers = {
    'William': 6,
    'Tome': 8,
    'Lily': 12,
    'Zuul': 24,
    'John': 10
}

for name in lucky_numbers.keys():
    print(name.title() + " like number " + str(lucky_numbers.get(name)))

for number in lucky_numbers.values():
    print("Lucky number: " + str(number))
