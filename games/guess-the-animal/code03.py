"""One trick pony
"""

from utils import explore_tree


meow_action  = {"kind" : "action",
                 "text" : "meow",
                 "yes" : {"kind" : "animal",
                          "text" : "cat"},
                 "no" :  {"kind" : "animal",
                          "text" : "dog"}}

decision_tree = {"kind" : "action",
                 "text" : "quack",
                 "yes" : {"kind" : "animal",
                          "text" : "duck"},
                 "no" :  meow_action}


explore_tree(decision_tree)