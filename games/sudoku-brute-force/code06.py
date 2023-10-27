"""Attempt to generate Sudoku via brute force 
"""
import numpy as np

from utils import shuffle_by_row, validate_matrix


ATTEMPTS = 1000
SUDOKU_SIZE = 4 # puzzle dimensions

# ordered grid
grid = np.tile(np.arange(1, SUDOKU_SIZE + 1), (SUDOKU_SIZE, 1))

# try randomly get a valid matrix
for _ in range(ATTEMPTS):
    shuffle_by_row(grid)
    if validate_matrix(grid):
        break

# which outcome?
if validate_matrix(grid):
    print(grid)
else:
    print("Ran out of attempts")
