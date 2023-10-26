"""Test identifiyng available values fror the cell.
"""

import numpy as np
from utils import coords_from_index

# puzzle dimensions
SUDOKU_SIZE = 4
BLOCK_SIZE = int(np.sqrt(SUDOKU_SIZE))

# defining an example matrix
example_matrix = np.zeros((SUDOKU_SIZE, SUDOKU_SIZE))
example_matrix[1, 1] = 1
example_matrix[2, 2] = 2
example_matrix[3, 1] = 2
example_matrix[3, 0] = 4

# figure out coordinates
row, col, block_row, block_col = coords_from_index(9, SUDOKU_SIZE)

# get unique values
values_in_row = np.unique(example_matrix[row, :])
values_in_col = np.unique(example_matrix[:, col])
values_in_block = np.unique(example_matrix[(block_row * BLOCK_SIZE):(block_row * BLOCK_SIZE + BLOCK_SIZE),
                                           (block_col * BLOCK_SIZE):(block_col * BLOCK_SIZE + BLOCK_SIZE)])
already_used = np.union1d(np.union1d(values_in_row, values_in_col), values_in_block)

# find the remaining available values
print(np.setdiff1d(np.arange(SUDOKU_SIZE + 1), already_used))
