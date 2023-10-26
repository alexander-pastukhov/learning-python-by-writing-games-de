"""Test shuffling columns.
"""

import numpy as np

from utils import shuffle_by_column


# puzzle dimensions
SUDOKU_SIZE = 9

# ordered grid
col_vector = np.transpose([np.arange(1, SUDOKU_SIZE + 1)])
grid = np.repeat(col_vector, SUDOKU_SIZE, axis=1)

# shuffle
shuffle_by_column(grid)
print(grid)
