"""Utilities for the minesweeper game
"""

import numpy as np

def input_coords(field_size):
    """Get valid cell coordinates.

    Parameters
    ----------
    field_size : int


    Returns
    ----------
    tuple
    """
    # list of valid letters
    row_letters = [chr(ord("A") + i) for i in range(field_size)]

    # asking
    coords = input("Please enter cell coordinates: ")

    while not (len(coords) == 2 and \
               coords[0].upper() in row_letters and \
               coords[1].isdigit() and int(coords[1]) >= 1 and int(coords[1]) <= field_size):
        coords = input("Please enter cell coordinates: ")
    
    return (ord(coords[0].upper()) - ord("A"), int(coords[1]) - 1)


def print_minefield(minefied):
    """Print minefield.

    Parameters
    ----------
    minefield : np.array
    """
    columns = '  ' + ''.join(np.arange(1, minefied.shape[0] + 1).astype(str))


    print(columns)
    print("  " + "".join(["-"] * (minefied.shape[0])))
    for irow in range(minefied.shape[0]):
        print(chr(ord("A") + irow) + "|", end="")
        for cell in minefied[irow, ]:
            if cell in ["*", " "]:
                print("•", end="")
            else:
                print(cell, end="")
        print()  


def count_mines(minefield, coords):
    """Count mines in surrounding cells.

    Parameters
    ----------
    minefield : np.array
    coords : tuple

    Returns
    ----------
    int
    """
    # figuring out slice limits given the edge problem
    left = max(coords[1] - 1, 0)
    right = min(coords[1] + 2, minefield.shape[1])
    top = max(coords[0] - 1, 0)
    bottom = min(coords[0] + 2, minefield.shape[0])

    return np.sum(minefield[top:bottom, left:right] == "*")


def count_mines_and_fill(minefield, coords):
    """Count mines in surrounding cells.

    Parameters
    ----------
    minefield : np.array
    coords : tuple

    Returns
    ----------
    int
    """


    # figuring out slice limits given the edge problem
    left = max(coords[1] - 1, 0)
    right = min(coords[1] + 2, minefield.shape[1])
    top = max(coords[0] - 1, 0)
    bottom = min(coords[0] + 2, minefield.shape[0])

    mine_count = np.sum(minefield[top:bottom, left:right] == "*")
    minefield[coords[0], coords[1]] = mine_count

def count_mines_and_spread(minefield, coords):
    """Count mines in surrounding cells and
    repeat for neigbouring cells if count is zero.

    Parameters
    ----------
    minefield : np.array
    coords : tuple

    Returns
    ----------
    int
    """
    # didn't we do it already?
    if minefield[coords[0], coords[1]] != " ":
        return

    # figuring out slice limits given the edge problem
    left = max(coords[1] - 1, 0)
    right = min(coords[1] + 2, minefield.shape[1])
    top = max(coords[0] - 1, 0)
    bottom = min(coords[0] + 2, minefield.shape[0])

    mine_count = np.sum(minefield[top:bottom, left:right] == "*")
    minefield[coords[0], coords[1]] = mine_count

    # do we need to spread the word?
    if mine_count == 0:
        for irow in range(top, bottom):
            for icol in range(left, right):
                count_mines_and_spread(minefield, (irow, icol))
