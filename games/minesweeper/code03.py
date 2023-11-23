"""Test count_mines function.
"""

import numpy as np

from utils import count_mines

a_minefield = np.array(
  [[' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' '],
   [' ', ' ', '*', ' ', '*'],
   [' ', ' ', '*', ' ', '*'],
   [' ', '*', ' ', ' ', ' ']], dtype='<U1')


print(count_mines(a_minefield, (4, 2)))
