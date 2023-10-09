#!/usr/bin/python3
""" This module contains one method `lookup(obj)` that prints all
    attributes available for an object
"""


def lookup(obj):
    """a function that returns the list
    of available attributes and methods of an object
    """
    return dir(obj)
