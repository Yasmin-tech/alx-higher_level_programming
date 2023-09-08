#!/usr/bin/python3
def element_at(my_list, idx):
    """ a function that retrieves an element from a list like in C
    """
    _len = len(my_list)
    if idx < 0 or idx >= _len:
        return None
    else:
        return my_list[idx]
