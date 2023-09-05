#!/usr/bin/python3
def pow(a, b):
    """ a function that computes a to the power of b and return the value

        Return: a ^ b
    """
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("Both, a and b must be numbers")

    _pow = a ** b
    return _pow
