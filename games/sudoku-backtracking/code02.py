"""Testing computation for row and column cell and block index
"""

from utils import coords_from_index


# puzzle dimensions
SUDOKU_SIZE = 4

# test for index 9
print(coords_from_index(9, SUDOKU_SIZE))
