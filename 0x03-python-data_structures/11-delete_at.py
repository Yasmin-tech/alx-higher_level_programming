#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ a function that deletes the item at a specific position in a list.

    """
    _len = len(my_list)

    if idx < 0 or idx >= _len:
        return my_list

    for index, item in enumerate(my_list):
        if index == idx:
            my_list.remove(item)

    return my_list
