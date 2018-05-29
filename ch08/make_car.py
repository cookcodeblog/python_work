# 8-14 Make Car


def make_car(vendor, type, **args):
    car = {'vendor': vendor, 'type': type}
    for key, value in args.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
