def islower(c):
    """a function that checks for lowercase character

    return True if c is lowercase character and False otherwise
    """

    if isinstance(c, int):
        return False

    if isinstance(c, str):
        ascii_repres = ord(c)
        if ascii_repres >= 97 and ascii_repres <= 122:
            return True
        else:
            return False
    else:
        return False


print(islower.__doc__)
