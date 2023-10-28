"""One trick pony
"""

from utils import explore_and_modify_tree


decision_tree = {"kind" : "animal",
                 "text" : "dog"}

while True:
    explore_and_modify_tree(decision_tree)
    print(decision_tree)
