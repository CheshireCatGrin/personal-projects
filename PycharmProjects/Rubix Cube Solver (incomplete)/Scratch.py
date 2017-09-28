import math
import itertools
#from Utilities import solvecross
from Utilities import generate_opp_coords
from Rubix import Rubix
#from Path import Path
from copy import deepcopy

test_rubix = Rubix()
win_rubix = Rubix()

test_rubix_sides = [("F", ['O', 'R', 'R', 'B', 'Y', 'O', 'Y', 'W', 'B']),
                    ("B", ['W', 'R', 'O', 'O', 'W', 'Y', 'O', 'G', 'G']),
                    ("U", ['B', 'Y', 'G', 'O', 'B', 'G', 'Y', 'G', 'W']),
                    ("D", ['G', 'O', 'R', 'R', 'G', 'R', 'W', 'Y', 'Y']),
                    ("R", ['B', 'W', 'R', 'Y', 'O', 'G', 'Y', 'W', 'B']),
                    ("L", ['W', 'B', 'G', 'B', 'R', 'W', 'O', 'B', 'R'])]

win_rubix_sides = [("F", ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']),
                   ("B", ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']),
                   ("U", ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']),
                   ("D", ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']),
                   ("R", ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']),
                   ("L", ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'])]

colors_list = ["Y", "W", "B", "R", "G", "O"]
test_rubix.colors = colors_list
win_rubix.colors = colors_list

test_rubix.update_coords(test_rubix_sides)
win_rubix.update_coords(win_rubix_sides)

orig_rubix = deepcopy(test_rubix)

list_of_states = [orig_rubix.coords]
list_of_rotations = ["F", "Fi", "B", "Bi", "U", "Ui", "D", "Di", "L", "Li", "R", "Ri"]
list_of_instructions = []
i = 0

test_opp_colors = [["W", "Y"], ["B", "G"], ["R", "O"]]

