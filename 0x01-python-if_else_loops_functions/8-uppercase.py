#!/usr/bin/python3
def uppercase(str):
    """\
    a function that prints a string in uppercase followed by a new line.

    """
    new_str = ""
    for ch in str:
        ascii_represent = ord(ch)
        if ascii_represent >= 97 and ascii_represent <= 122:
            new_str += chr(ascii_represent - 32)
        else:
            new_str += ch

    print("{}".format(new_str))
