#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ Write a function that replaces or adds key/value in a dictionary.

    Arguments:
            a_dictionary
            key argument will be always a string
            value argument will be any type

    Return:
            a_dictionary after update
    """
    a_dictionary.update({key: value})
    return a_dictionary
