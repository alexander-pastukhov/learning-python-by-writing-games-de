"""Collection of utilities for the Sudoku backtracking algorithm.

Functions
---------
row_col_from_index(index, row_width)
    Compute row and column index from the overall index.
coords_from_index(index, row_width)
    Compute row and column index for cell block from overall index.
get_available_values(grid, icell, sudoku_size, block_size)
    Get values still available for the cell.
add_one_cell(grid, icell, sudoku_size, block_size)
    Add a random value to a cell using available numbers.
add_few_cells(grid, remaining_cells, sudoku_size, block_size)
    Add a random value to a cell using available numbers.
    Modifies matrix in place, continues recursively,
    until the matrix is complete. No backtracking!
add_cell(grid, remaining_cells, sudoku_size, block_size)
    Add a random value to a cell using available numbers.
    Modifies matrix in place, continues recursively,
    until the matrix is complete.
"""

import numpy as np


class GridComplete(Exception):
    pass


def row_col_from_index(index, row_width):
    """Compute row and column index from the overall index.

    Parameters
    ----------
    index : int
    row_width : int

    Returns
    ----------
    tuple : (row, col) index
    """
    row = index // row_width
    col = index % row_width

    return (row, col)


def coords_from_index(index, row_width):
    """Compute row and column index for cell and block from overall index.

    Parameters
    ----------
    index : int
    row_width : int

    Returns
    ----------
    tuple : (row, col, block_row, block_index) index
    """
    block_width = int(np.sqrt(row_width))
    row = index // row_width
    col = index % row_width

    block_row = row // block_width
    block_col = col // block_width

    return (row, col, block_row, block_col)


def get_available_values(grid, icell, sudoku_size, block_size):
    """Get values still available for the cell.

    Parameters
    ----------
    grid : numpy.array
        matrix sudoku_size x sudoku_size
    icell : int
        cell index
    sudoku_size : int
    block_size : int

    Returns
    ----------
    numpy.array
    """
    # figure out coordinates
    row, col, block_row, block_col = coords_from_index(icell, sudoku_size)

    # get unique values
    values_in_row = np.unique(grid[row, :])
    values_in_col = np.unique(grid[:, col])
    values_in_block = np.unique(grid[(block_row * block_size):(block_row * block_size + block_size),
                                     (block_col * block_size):(block_col * block_size + block_size)])
    already_used = np.union1d(np.union1d(values_in_row, values_in_col), values_in_block)

    # find the remaining available values
    return np.setdiff1d(np.arange(sudoku_size + 1), already_used)


def add_one_cell(grid, icell, sudoku_size, block_size):
    """Add a random value to a cell using available numbers.
    Modifies matrix in place.

    Parameters
    ----------
    grid : numpy.array
        matrix sudoku_size x sudoku_size
    icell : int
        cell index
    sudoku_size : int
    block_size : int
    """
    row, col, block_row, block_col = coords_from_index(icell, sudoku_size)

    # figure out values that were already used
    values_in_row = np.unique(grid[row, :])
    values_in_col = np.unique(grid[:, col])
    values_in_block = np.unique(grid[(block_row * block_size):(block_row * block_size + block_size),
                                     (block_col * block_size):(block_col * block_size + block_size)])
    already_used = np.union1d(np.union1d(values_in_row, values_in_col), values_in_block)

    # find available values
    available_values = np.setdiff1d(np.arange(sudoku_size + 1), already_used)

    # shuffle
    np.random.shuffle(available_values)

    # use the first one
    grid[row, col] = available_values[0]


def add_few_cells(grid, remaining_cells, sudoku_size, block_size):
    """Add a random value to a cell using available numbers.
        Modifies matrix in place, continues recursively,
        until the matrix is complete. No backtracking!

    Parameters
    ----------
    grid : numpy.array
    matrix sudoku_size x sudoku_size
    remaining_cells : list
    list of cell indexes for remaining cells
    sudoku_size : int
    block_size : int
    """
    # complete grid?
    if len(remaining_cells) == 0:
        raise GridComplete

    row, col, block_row, block_col = coords_from_index(remaining_cells[0], sudoku_size)

    # figure out values that were already used
    values_in_row = np.unique(grid[row, :])
    values_in_col = np.unique(grid[:, col])
    values_in_block = np.unique(grid[(block_row * block_size):(block_row * block_size + block_size),
                                     (block_col * block_size):(block_col * block_size + block_size)])
    already_used = np.union1d(np.union1d(values_in_row, values_in_col), values_in_block)

    # find available values
    available_values = np.setdiff1d(np.arange(sudoku_size + 1), already_used)

    # shuffle
    np.random.shuffle(available_values)

    # use the first one
    grid[row, col] = available_values[0]

    add_few_cells(grid, remaining_cells[1:], sudoku_size, block_size)


def add_cell(grid, remaining_cells, sudoku_size, block_size):
    """Add a random value to a cell using available numbers.
    Modifies matrix in place, continues recursively,
    until the matrix is complete.

    Parameters
    ----------
    grid : numpy.array
    matrix sudoku_size x sudoku_size
    remaining_cells : list
    list of cell indexes for remaining cells
    sudoku_size : int
    block_size : int
    """
    # complete grid?
    if len(remaining_cells) == 0:
        raise GridComplete

    # figure out alternative coordinate systems
    row, col, block_row, block_col = coords_from_index(remaining_cells[0], sudoku_size)

    # figure out values that were already used
    values_in_row = np.unique(grid[row, :])
    values_in_col = np.unique(grid[:, col])
    values_in_block = np.unique(grid[(block_row * block_size):(block_row * block_size + block_size),
                                    (block_col * block_size):(block_col * block_size + block_size)])
    already_used = np.union1d(np.union1d(values_in_row, values_in_col), values_in_block)

    # find available values
    available_values = np.setdiff1d(np.arange(1, sudoku_size + 1), already_used)

    # shuffle
    np.random.shuffle(available_values)

    # go through values, hoping that one of the works
    for value in available_values:
        grid[row, col] = value
        add_cell(grid, remaining_cells[1:], sudoku_size, block_size)

    # nope, dead end
    grid[row, col] = 0
    return

