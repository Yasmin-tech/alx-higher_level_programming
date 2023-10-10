#!/usr/bin/python3
""" This module contains one class `BaseGeometry`
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    methods
    -------
    __init__(self, width, height): initialize an object

    area(self): Return the area of the rectangle
    """

    def __init__(self, width, height):
        """initialize an object

        Args
        ----
        width : int
        height : int
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return str of the object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
