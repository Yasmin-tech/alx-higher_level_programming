#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ Write a function that replaces or adds key/value in a dictionary.

    Arguments:
        a_dictionary
        key of the pair to be removed

    Return:
        a_dictionary after the delete
    """
    if key not in a_dictionary:
        return a_dictionary
    del (a_dictionary[key])
    return a_dictionary
