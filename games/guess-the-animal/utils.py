"""Functions for Guess-the-Animal game.
"""

import copy


def input_yes_no(prompt):
    """Get [y]es/[n]o answer.

    Parameters
    ----------
    prompt : str


    Returns
    ----------
    logical
    """

    response = ""
    while response not in ["n", "y"]:
        response = input('Type "y" for yes and "n" for no. ' + prompt)

    return response == "y"


def ask_question(tree):
    """Ask question depending on the top node kind.

    Parameters
    ----------
    tree : dict
    """
    if tree["kind"] == "animal":
        if input_yes_no("Is this " + tree["text"] + "?"):
            print("I knew it!")
    else:
        input_yes_no("Does it " + tree["text"] + "?")


def explore_tree(tree):
    """Explore decision tree, no update.

    Parameters
    ----------
    tree : dict
    """
    if tree["kind"] == "animal":
        if input_yes_no("Is this " + tree["text"] + "?"):
            print("I knew it!")
    else:
        action_response = "yes" if input_yes_no("Does it " + tree["text"] + "?") else "no"
        explore_tree(tree[action_response])

def explore_and_extend_tree_via_return(tree):
    """Explore decision tree, update via new reference.

    Parameters
    ----------
    tree : dict

    Returns
    ----------
    dict : original or updated (sub)tree
    """
    if tree["kind"] == "animal":
        if input_yes_no("Is this " + tree["text"] + "?"):
            print("I knew it!")
        else:
            # extending the tree
            new_animal_text = input("Who is it?")
            new_animal = {"kind" : "animal", "text" : new_animal_text}

            new_action_text = input("What does " + new_animal_text + " do?")
            new_action = {"kind" : "action",
                        "text" : new_action_text,
                        "yes" : new_animal,
                        "no" : tree}
            return new_action
    else:
        action_response = "yes" if input_yes_no("Does it " + tree["text"] + "?") else "no"
        tree[action_response] = explore_and_extend_tree_via_return(tree[action_response])
    return tree


def explore_and_modify_tree(tree):
    """Explore decision tree, update in place

    Parameters
    ----------
    tree : dict
    """
    if tree["kind"] == "animal":
        if input_yes_no("Is this " + tree["text"] + "?"):
            print("I knew it!")
        else:
            # extending the tree
            old_animal = copy.deepcopy(tree)
            new_animal_text = input("Who is it? ")
            new_animal = {"kind" : "animal", "text" : new_animal_text}

            new_action_text = input("What does " + new_animal_text + " do? ")
            tree["kind"] = "action"
            tree["text"] = new_action_text
            tree["yes"] =  new_animal
            tree["no"] = old_animal
    else:
        action_response = "yes" if input_yes_no("Does it " + tree["text"] + "?") else "no"
        explore_and_modify_tree(tree[action_response])

