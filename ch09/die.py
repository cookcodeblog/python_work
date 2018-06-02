# 9-14 Die
from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        side = randint(1, self.sides)
        print("Side is " + str(side))


die6 = Die()
for num in range(0, 10):
    die6.roll_die()

print("####")


die10 = Die(10)
for num in range(0, 10):
    die10.roll_die()

print("###")
die20 = Die(20)
for num in range(0, 10):
    die20.roll_die()
