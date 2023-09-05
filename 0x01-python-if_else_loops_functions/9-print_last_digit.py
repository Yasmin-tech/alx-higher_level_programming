#!/usr/bin/python3
def print_last_digit(number):
    """ a function that prints the last digit of a number.

        Return: Last Digit in the number
    """
    num_str = str(number)
    print(num_str[-1], end="")
    return num_str[-1]
