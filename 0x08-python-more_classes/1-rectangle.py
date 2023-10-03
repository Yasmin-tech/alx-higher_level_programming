#!/usr/bin/python3
""" This Module contains the class Rectangle that defines a rectangle"""


class Rectangle:
    """ A class that defines a rectangle
    ......

    Attributes
    ------------

    width : int
            the width of the rectangle
    height : int
            the height of the rectangle

    Methods
    -------

    def __init__(self, width=0, height=0)
            A constructor to a new rectangle object

    def width(self):
            The getter method to retrieve the width property

   def width(self, value):
            The setter method to set the width property

   def height(self):
            The getter method to retrieve the height property

   def height(self, value):
            The setter method to set the height property

    """

    def __init__(self, width=0, height=0):
        """ A constructor to a new rectangle object.

        Args:
                self: the oject

                width : int
                The width of the rectangle

                height : int
                The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The getter method to retrieve the width property.

        Args:
                self: the object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ The setter method to set the width property.

        Args:
                self: the object

                value: int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ The getter method to retrieve the heigjt property.

        Args:
                self: the object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ The setter method to set the height property.

        Args:
                self: the object

                value: int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
