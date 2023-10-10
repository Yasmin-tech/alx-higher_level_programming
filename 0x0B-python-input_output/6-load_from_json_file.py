#!/usr/bin/python3
""" This module contains a function that loads a json file
        into a python code
"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a `JSON file`

    Args
    ----
            my_obj: a python code
            filename: a file with .json extention
    """
    with open(filename, "r") as f:
        obj = json.load(f)
        return obj
