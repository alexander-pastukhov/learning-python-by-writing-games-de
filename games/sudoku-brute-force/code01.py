"""Test shuffling rows.
"""

import numpy as np

from utils import shuffle_by_row


# puzzle dimensions
SUDOKU_SIZE = 9

# ordered grid
grid = np.tile(np.arange(1, SUDOKU_SIZE + 1), (SUDOKU_SIZE, 1))

# shuffle
shuffle_by_row(grid)
print(grid)
