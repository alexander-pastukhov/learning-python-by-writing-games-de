"""One trick pony
"""

from utils import explore_and_modify_tree, input_yes_no


decision_tree = {"kind" : "animal",
                 "text" : "dog"}

wanna_play = True
while wanna_play:
    explore_and_modify_tree(decision_tree)
    print(decision_tree)

    wanna_play = input_yes_no("Do you want to play again?")
