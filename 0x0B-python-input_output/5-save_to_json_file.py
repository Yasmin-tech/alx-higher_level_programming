#!/usr/bin/python3
""" This module contains a function that saves
         the python code as a string to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file
    using a JSON representation

    Args
    ----
            my_obj: a python code
            filename: a file with .json extention
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
