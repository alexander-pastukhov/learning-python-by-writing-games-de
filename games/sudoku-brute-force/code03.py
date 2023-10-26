"""Test shuffling rows and row validation.
"""

import numpy as np

from utils import shuffle_by_row, validate_rows


# puzzle dimensions
SUDOKU_SIZE = 9

# ordered grid
grid = np.tile(np.arange(1, SUDOKU_SIZE + 1), (SUDOKU_SIZE, 1))

# shuffle
shuffle_by_row(grid)
print(grid)

# check that rows are the valid
print(validate_rows(grid))
