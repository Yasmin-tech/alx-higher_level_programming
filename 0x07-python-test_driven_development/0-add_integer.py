#!/usr/bin/python3
""" This module contain only one function `add_integer(a, b)`


The function calculates and return the addition of the two arrguments
"""


def add_integer(a, b=98):
    """
        a function that calculates and return the addition of the two arguments
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
