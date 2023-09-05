#!/usr/bin/python3
def islower(c):
    """a function that checks for lowercase character

    return True if c is lowercase character and False otherwise
    """
    try:
        ascii_repres = ord(c)
        if ascii_repres >= 97 and ascii_repres <= 122:
            return True
        else:
            return False
    except TypeError:
        return False


# print(islower.__doc__)
