"""One trick pony
"""

from utils import input_yes_no

decision_tree = {"kind" : "action",
                 "text" : "quack",
                 "yes" : {"kind" : "animal",
                          "text" : "duck"},
                 "no" :  {"kind" : "animal",
                          "text" : "dog"}}

if decision_tree["kind"] == "animal":
    if input_yes_no("Is this " + decision_tree["text"] + "?"):
        print("I knew it!")
else:
    input_yes_no("Does it " + decision_tree["text"] + "?")
