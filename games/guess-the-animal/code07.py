"""One trick pony
"""
import pickle
from utils import explore_and_modify_tree, input_yes_no

with open("tree01.p", "rb") as pickle_file:
  decision_tree = pickle.load(pickle_file)

wanna_play = True
while wanna_play:
    explore_and_modify_tree(decision_tree)
    print(decision_tree)

    wanna_play = input_yes_no("Do you want to play again?")

with open("tree01.p", "wb") as pickle_file:
  pickle.dump(decision_tree, pickle_file)
