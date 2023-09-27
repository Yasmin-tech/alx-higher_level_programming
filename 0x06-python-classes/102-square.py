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

    def __eq__(self, ob_2: object) -> bool:
        """ a private method to compare if two Square objects are equal """
        return self.__size == ob_2.__size

    def __ne__(self, ob_2: object) -> bool:
        """ a private method to compare if two Square objects are not equal """
        return self.__size != ob_2.__size

    def __lt__(self, ob_2: object) -> bool:
        """ a private method to compare if object 1 is less than object 2 """
        return self.__size < ob_2.__size

    def __le__(self, ob_2: object) -> bool:
        """ a private method to compare if object 1 <= object 2 """
        return self.__size <= ob_2.__size

    def __gt__(self, ob_2: object) -> bool:
        """ a private method to compare if object 1 > object 2 """
        return self.__size > ob_2.__size

    def __ge__(self, ob_2: object) -> bool:
        """ a private method to compare if object 1 >= object 2 """
        return self.__size >= ob_2.__size
