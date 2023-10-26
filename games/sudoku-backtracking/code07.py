"""Placing value into a single cell
"""

import numpy as np
from utils import add_one_cell

SUDOKU_SIZE = 4
BLOCK_SIZE = int(np.sqrt(SUDOKU_SIZE))

# empty grid  
grid = np.zeros((SUDOKU_SIZE, SUDOKU_SIZE))

# fix randomness
np.random.seed(42)

# random walk through the matrix
indexes = np.arange(SUDOKU_SIZE * SUDOKU_SIZE)
np.random.shuffle(indexes)

# place a single cell
add_one_cell(grid, indexes[0], SUDOKU_SIZE, BLOCK_SIZE)

print(grid)
