"""Collection of function for Sudoku brute force algorithm.
"""

import numpy as np


def shuffle_by_row(grid):
    """Shuffled each row of the matrix.

    Parameters
    ----------
    grid: numpy.array
        2D grid
    """

    for irow in range(grid.shape[0]):
        np.random.shuffle(grid[irow, :])


def shuffle_by_column(grid):
    """Shuffled each column of the matrix.

    Parameters
    ----------
    grid: numpy.array
        2D grid
    """

    for icol in range(grid.shape[1]):
        np.random.shuffle(grid[:, icol])


def validate_rows(grid):
    """Check whether all rows are valid.

    Parameters
    ----------
    grid: numpy.array
        2D grid

    Returns
    ----------
    logical
    """
    row_validity = [np.unique(grid[irow, :]).size == grid.shape[0]
                    for irow in range(grid.shape[0])]
    return np.all(row_validity)


def validate_columns(grid):
    """Check whether all columns are valid.

    Parameters
    ----------
    grid: numpy.array
        2D grid

    Returns
    ----------
    logical
    """
    col_validity = [np.unique(grid[:, icol]).size == grid.shape[0]
                    for icol in range(grid.shape[1])]
    return np.all(col_validity)
