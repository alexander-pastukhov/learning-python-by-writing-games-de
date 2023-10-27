"""Test shuffling rows and row/column validation.
"""

import numpy as np

from utils import shuffle_by_row, validate_rows, validate_columns, validate_blocks

all_valid = np.array([[4, 1, 3, 2],
                      [3, 2, 4, 1],
                      [2, 4, 1, 3],
                      [1, 3, 2, 4]])
print(validate_rows(all_valid), validate_columns(all_valid), validate_blocks(all_valid))

invalid_row = np.array([[4, 1, 3, 1],
                        [3, 2, 4, 2],
                        [2, 4, 1, 3],
                        [1, 3, 2, 4]])
print(validate_rows(invalid_row), validate_columns(invalid_row), validate_blocks(invalid_row))

invalid_column = np.array([[4, 1, 3, 2],
                           [3, 2, 1, 4],
                           [2, 4, 1, 3],
                           [1, 3, 2, 4]])
print(validate_rows(invalid_column), validate_columns(invalid_column), validate_blocks(invalid_column))

invalid_block_and_column = np.array([[4, 3, 1, 2],
                                     [3, 2, 4, 1],
                                     [2, 4, 1, 3],
                                     [1, 2, 3, 4]])
print(validate_rows(invalid_block_and_column),
      validate_columns(invalid_block_and_column),
      validate_blocks(invalid_block_and_column))

invalid_block_and_row = np.array([[4, 1, 3, 2],
                                  [3, 4, 4, 1],
                                  [2, 2, 1, 3],
                                  [1, 3, 2, 4]])
print(validate_rows(invalid_block_and_row),
      validate_columns(invalid_block_and_row),
      validate_blocks(invalid_block_and_row))

all_invalid = np.array([[4, 1, 3, 2],
                        [3, 4, 1, 4],
                        [2, 2, 1, 3],
                        [1, 3, 2, 4]])
print(validate_rows(all_invalid),
      validate_columns(all_invalid),
      validate_blocks(all_invalid))
