# 8-5 describe_city() function


def describe_city(city, country="China"):
    print(str(city).title() + " is in " + country.title())


describe_city("Shanghai")
describe_city("Beijing")
describe_city(city="Chongqing")
describe_city("London", "England")
describe_city(city="California", country="America")

