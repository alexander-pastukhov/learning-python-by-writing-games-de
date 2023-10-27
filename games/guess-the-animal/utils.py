"""Functions for Guess-the-Animal game.
"""


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