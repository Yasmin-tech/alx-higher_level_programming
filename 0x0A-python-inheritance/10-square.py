#!/usr/bin/python3
""" This module contains one class `BaseGeometry`
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class

    methods
    -------
    __init__(self, size): initialize an object

    area(self): Return the area of the square
    """

    def __init__(self, size):
        """initialize an object

        Args
        ----
        size : int
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size**2

    def __str__(self):
        """return str of the object"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
