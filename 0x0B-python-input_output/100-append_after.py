#!/usr/bin/python3
""" A module that contains one function that modefy a file by adding

the desired string after a specific string was found
"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r") as f:
        list_lines = f.readlines()

    new_list = ""
    for line in list_lines:
        new_list += line
        if search_string in line:
            new_list += new_string
    with open(filename, "w") as f:
        f.writelines(new_list)
