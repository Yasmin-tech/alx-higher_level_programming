#!/usr/bin/python3
def add(a, b):
    """ a function that adds two integers and returns the result.

        Return: a + b
    """
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("Both, a and b must be numbers")

    sum = a + b
    return sum
