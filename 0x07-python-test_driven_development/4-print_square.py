#!/usr/bin/python3
""" This module contains one function `rint_square(size)`


Thefunction that prints a square with the character #.
"""


def print_square(size):
    """ a function that prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i != size - 1:
            print("")
    print("")
