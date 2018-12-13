from random import randint


class Die:
    """Represent a die."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))
# NOTE: 6 sided die
# dice = Die()

# NOTE: 10-sided die
# dice = Die(10)
# NOTE: 20-sided die
dice = Die(20)


dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
