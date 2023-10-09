#!/usr/bin/python3
""" This module contains one method `is_kind_of_class(obj, a_class)`
"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
