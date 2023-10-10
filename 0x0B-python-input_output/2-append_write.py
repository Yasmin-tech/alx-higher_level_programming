#!/usr/bin/python3
""" In this module, we have a function that opens a file to add to its content

if the file does not exist, it will be created
"""


def append_write(filename="", text=""):
    """a function that appends a string to a text file (UTF8)

    Return
    -------
         the number of characters written
    """
    with open(filename, "a", encoding="UTF8") as f:
        char_writen = f.write(text)
        return char_writen
