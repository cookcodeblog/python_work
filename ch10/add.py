# 10-6 Add


def add(_left_num, _right_num):
    try:
        return int(_left_num) + int(_right_num)
    except ValueError:
        try:
            return float(_left_num) + float(_right_num)
        except ValueError:
            print("Please ensure input both valid numbers: [" + str(_left_num) + "] + [" + str(_right_num) + "]")


left_num = input("Please input a number: ")
right_num = input("Please input another number: ")
print("The result is: " + str(add(left_num, right_num)))
