#!/usr/bin/python3
def no_c(my_string):
    """ a function that removes all characters c and C from a string

    """
    list_char = list(my_string)
    for char in list_char:
        if char in "cC":
            list_char.remove(char)

    new_string = "".join(list_char)
    return (new_string)
