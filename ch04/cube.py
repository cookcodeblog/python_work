# 4-8 Cube
# Print cube for numbers from 1 to 10

for number in range(1, 11):
    print("cube(" + str(number) + ") is " + str(number ** 3))

print()

cube_numbers = [number ** 3 for number in range(1, 11)]
print(cube_numbers)