#!/usr/bin/python3
""" This module defines the class MyInt that inherits from int
"""


class MyInt(int):
    """ " a class MyInt that inherits from int.

    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, __value: object) -> bool:
        """if two objects are equal, this function will
        return False
        """
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """if two objects are not equal, this function will
        return True
        """
        return super().__eq__(__value)
