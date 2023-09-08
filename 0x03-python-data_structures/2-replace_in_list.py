#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ a function that replaces an element of a list

    replaces an element at a specific position (like in C)
    """
    _len = len(my_list)
    if idx < 0 or idx >= _len:
        return my_list
    my_list[idx] = element
    return my_list
