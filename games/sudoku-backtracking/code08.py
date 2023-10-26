"""Sudoku: filling few cells with backtracking mechanism.
"""

import numpy as np

from utils import GridComplete, add_few_cells


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
    add_few_cells(grid, indexes[:4], SUDOKU_SIZE, BLOCK_SIZE)
except GridComplete:
    pass

print(grid)
