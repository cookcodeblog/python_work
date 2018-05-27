# 6-11 Cities


guangzhou = {
    'name': 'Guangzhou',
    'country': 'China',
    'population': '20 million',
    'fact': "The city's nick name is flower city."
}


toronto = {
    'name': 'Toronto',
    'country': 'Canada',
    'population': '6 million',
    'fact': "The economy centre of Canada."
}

athens = {
    'name': 'Athens',
    'country': 'Greece',
    'population': '700 k',
    'fact': 'A famous city in Europe.'
}


cities = {
    'guangzhou': guangzhou,
    'toronto': toronto,
    'athens': athens
}

for name, city in cities.items():
    print(name.title() + " is one of cities of " + city['country'].title() + ".")
    print(name.title() + "'s population is " + city['population'] + ".")
    print("A fact of " + name.title() + " is: " + city['fact'] + "\n")
