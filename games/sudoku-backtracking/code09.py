"""Sudoku: complete backtracking mechanism.
"""

import numpy as np

from utils import GridComplete, add_cell


# puzzle dimensions
SUDOKU_SIZE = 4
BLOCK_SIZE = int(np.sqrt(SUDOKU_SIZE))


# empty grid
grid = np.zeros((SUDOKU_SIZE, SUDOKU_SIZE))


# fix randomness
np.random.seed(1100)


# random walk through the matrix
indexes = np.arange(SUDOKU_SIZE * SUDOKU_SIZE)
np.random.shuffle(indexes)

try:
    # place a single cell
    add_cell(grid, indexes, SUDOKU_SIZE, BLOCK_SIZE)
except GridComplete:
    pass

print(grid)
