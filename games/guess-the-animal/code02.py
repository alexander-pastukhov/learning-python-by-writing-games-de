"""One trick pony
"""

from utils import ask_question

decision_tree = {"kind" : "action",
                 "text" : "quack",
                 "yes" : {"kind" : "animal",
                          "text" : "duck"},
                 "no" :  {"kind" : "animal",
                          "text" : "dog"}}

ask_question(decision_tree)
