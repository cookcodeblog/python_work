# 6-9 Favorite Places

favorite_places = {
    'William': ["Hainan", "Guangzhou", "Yunnan"],
    'Sunna': ["Shanxi", "Greece", "London"],
    'Wilson': ["Shanghai", "Beijing", "Hong Kong"]
}

for name, places in favorite_places.items():
    print(name.title() + " likes following places:")
    for place in places:
        print("\t" + place.title())
    print()



