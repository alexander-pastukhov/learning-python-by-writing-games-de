"""Creating a minefield and printing it out.
"""

import numpy as np
from utils import print_minefield

FIELD_SIZE = 5
MINES_N = 1


# create an empty field
field = np.full((FIELD_SIZE, FIELD_SIZE), ' ')

np.random.seed(42)

# place mines
for _ in range(MINES_N):
    # finding a vacant spot
    xy = np.random.randint(0, FIELD_SIZE, 2)
    while field[xy[0], xy[1]] == "*":
        xy = np.random.randint(0, FIELD_SIZE, 2)
    field[xy[0], xy[1]] = "*"

# print out
print_minefield(field)