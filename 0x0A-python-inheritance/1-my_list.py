#!/usr/bin/python3
""" This module contains one class `MyList`

It inharetice from the base class `list` and defines one public method
`print_sorted(self)` that prints the list in ascending sort
"""


class MyList(list):
    """a class that inherantce from list

    methods
    -------

    print_sored(self) -> void
    Public instance method:that prints the list in ascending sort
    """

    def __init__(self):
        """initializes the object"""
        super().__init__(self)

    def print_sorted(self):
        """prints the list in ascending sort."""
        print(sorted(self))
