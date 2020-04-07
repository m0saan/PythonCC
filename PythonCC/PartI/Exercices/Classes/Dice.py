from random import randint


class Die():

    def __init__(self, sides=6):
        """ Creating a dice game. """
        self.sides = sides

    def roll_die(self):
        randNumber = randint(1, self.sides)
        print(randNumber)


m_die = Die()
for n in range(10):
    m_die.roll_die()

m_die.sides = 10
for n in range(10):
    m_die.roll_die()


m_die.sides = 20
for n in range(10):
    m_die.roll_die()
