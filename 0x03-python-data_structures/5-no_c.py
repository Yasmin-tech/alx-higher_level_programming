#!/usr/bin/python3
def no_c(my_string):
    """ a function that removes all characters c and C from a string

    """
    list_char = [char for char in my_string if char not in "Cc"]

    new_string = "".join(list_char)
    return (new_string)
