"""Testing computation for row and column index
"""

from utils import row_col_from_index


# puzzle dimensions
SUDOKU_SIZE = 4

# test for index 9
print(row_col_from_index(9, SUDOKU_SIZE))
