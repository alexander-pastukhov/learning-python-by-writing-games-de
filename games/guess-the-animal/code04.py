"""One trick pony
"""

from utils import explore_and_extend_tree_via_return


decision_tree = {"kind" : "animal",
                 "text" : "dog"}

while True:
    decision_tree = explore_and_extend_tree_via_return(decision_tree)
    print(decision_tree)
