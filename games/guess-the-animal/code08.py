"""One trick pony
"""
import json
from utils import explore_and_modify_tree, input_yes_no

with open("tree01.json", "r") as json_file:
  decision_tree = json.load(json_file) 

wanna_play = True
while wanna_play:
    explore_and_modify_tree(decision_tree)
    print(decision_tree)

    wanna_play = input_yes_no("Do you want to play again?")

with open("tree01.json", "w") as json_file:
  json.dump(decision_tree, json_file)
