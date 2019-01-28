from random import randint


class Die:
    """Represent a die."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# Die exercises

# 6 sided die
# dice = Die()

# 10-sided die
# dice = Die(10)

# 20-sided die
# dice = Die(20)

# Roll die x times
# for i in range(dice.sides + 1):
#     print('Rolled: ')
#     dice.roll_die()
