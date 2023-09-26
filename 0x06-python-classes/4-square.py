#!/usr/bin/python3
""" a module that represente a class Square """


class Square:
    """ a class Square that defines a square. """

    def __init__(self, size=0) -> None:
        """ Instantiation of class Square
        """
        self.size = size

    @property
    def size(self):
        """ getter method for size attribute. """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for size attribute. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ a method that returns the current square area. """

        return self.__size * self.__size
