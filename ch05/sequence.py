# 5-11 Sequence

for number in range(1, 10):
    if number not in (1, 2, 3):
        print(str(number) + "th")
    elif number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
