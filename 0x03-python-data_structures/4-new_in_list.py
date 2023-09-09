#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ a function that replaces an element in a list

    at a specific position without modifying the original list
    """

    new_list = my_list[:]
    _len = len(my_list)

    if idx < 0 or idx >= _len:
        return new_list

    new_list[idx] = element
    return new_list
