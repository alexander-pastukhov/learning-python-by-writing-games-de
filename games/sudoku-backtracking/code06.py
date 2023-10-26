"""Test identifiyng available values fror the cell function.
"""

import numpy as np
from utils import get_available_values

# puzzle dimensions
SUDOKU_SIZE = 4
BLOCK_SIZE = int(np.sqrt(SUDOKU_SIZE))

# defining an example matrix
example_matrix = np.zeros((SUDOKU_SIZE, SUDOKU_SIZE))
example_matrix[1, 1] = 1
example_matrix[2, 2] = 2
example_matrix[3, 1] = 2
example_matrix[3, 0] = 4

# test
print(get_available_values(example_matrix, 9, SUDOKU_SIZE, BLOCK_SIZE))
