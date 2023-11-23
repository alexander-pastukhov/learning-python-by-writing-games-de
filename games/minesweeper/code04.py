"""Minesweeper game.
"""
import numpy as np

from utils import print_minefield, input_coords, count_mines

FIELD_SIZE = 2
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

print(field)

game_state = "playing"
while game_state == "playing":
    # print out
    print_minefield(field)

    # ask for coordinates
    coords = input_coords(FIELD_SIZE)

    # check if boom
    if field[coords[0], coords[1]] == "*":
        game_state = "exploded"
    else:
        field[coords[0], coords[1]] = count_mines(field, coords)

    if np.sum(field == " ") == 0:
        game_state = "victory"

# end of game messages
if game_state == "victory":
    print("Congrats!")
else:
    print("Oh no!")
