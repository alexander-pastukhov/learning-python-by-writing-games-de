"""One trick pony
"""

from utils import input_yes_no

decision_tree = {"kind" : "animal",
                 "text" : "dog"}


if decision_tree["kind"] == "animal":
    if input_yes_no("Is this " + decision_tree["text"] + "?"):
        print("I knew it!")
