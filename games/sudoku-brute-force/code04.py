"""Test shuffling rows and row/column validation.
"""

import numpy as np

from utils import shuffle_by_row, validate_rows, validate_columns


# puzzle dimensions
SUDOKU_SIZE = 9

# ordered grid
grid = np.tile(np.arange(1, SUDOKU_SIZE + 1), (SUDOKU_SIZE, 1))

# shuffle
shuffle_by_row(grid)
print(grid)

# check that rows are the valid
print(validate_rows(grid))

# check that columns are the valid
print(validate_columns(grid))
