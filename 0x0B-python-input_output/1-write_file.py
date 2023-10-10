#!/usr/bin/python3
""" In this module, we have a function that opens a file to write to

if the file does not exist, it willbe created
"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)

    Return
    -------
         the number of characters written
    """
    with open(filename, "w", encoding="UTF8") as f:
        char_writen = f.write(text)
        return char_writen
