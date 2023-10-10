#!/usr/bin/python3
""" This module contains a function that returns the JSON

representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """a function that returns the JSON representation
    JSON representation of an object is (string)

    Args
    ----
    my_obj : a python object
    """
    return json.dumps(my_obj)
