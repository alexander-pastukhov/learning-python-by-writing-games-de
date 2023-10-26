"""Testing path randomization.
"""

import numpy as np
from utils import coords_from_index

SUDOKU_SIZE = 4

# fixing random numbers
np.random.seed(42)

# empty grid
grid = np.zeros((SUDOKU_SIZE, SUDOKU_SIZE))

# random path
indexes = np.arange(SUDOKU_SIZE * SUDOKU_SIZE)
np.random.shuffle(indexes)

# filling out the matrix to show the path
for ivisit, icell in enumerate(indexes, start=1):
    row, col, block_row, block_col = coords_from_index(icell, SUDOKU_SIZE)
    grid[row, col] = ivisit

print(grid)
