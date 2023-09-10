#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ a function that prints all integers of a list,

    in reverse order.
    """
    if not my_list:
        return
    idx = len(my_list) - 1
    for i in range(idx, -1, -1):
        print("{:d}".format(my_list[i]))
