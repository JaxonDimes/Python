from random import randint


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        numberSided = randint(1, self.sides)
        print(f"Your request was a {self.sides}-sided die.")
        print(f"Here is your d{self.sides} roll: {numberSided}\n")


d_six = Die(6)
d_twenty = Die(20)

for num in range(1,11):
    d_six.roll_die()
    d_twenty.roll_die()





