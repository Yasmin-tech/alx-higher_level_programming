#!/usr/bin/python3
def max_integer(my_list=[]):
    """" a function that finds the biggest integer of a list. """

    _max = 0
    for num in my_list:
        if num > _max:
            _max = num

    return _max
