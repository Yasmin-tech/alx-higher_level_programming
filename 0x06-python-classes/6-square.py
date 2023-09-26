#!/usr/bin/python3
""" a module that represente a class Square """


class Square:
    """ a class Square that defines a square. """

    def __init__(self, size=0, position=(0, 0)) -> None:
        """ Instantiation of class Square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ a getter method for position attribute. """
        return self.__position

    @position.setter
    def position(self, new_tuple):
        """ a setter method for position attribute. """

        if not isinstance(new_tuple, tuple)\
                or new_tuple[0] < 0\
                or new_tuple[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = new_tuple

    def area(self):
        """ a method that returns the current square area. """

        return self.__size * self.__size

    def my_print(self):
        """ prints the square in # to stdout. """
        n = self.__size
        spaces = self.__position[0]
        for i in range(n):
            for k in range(spaces):
                print(" ", end="")
            for j in range(n):
                print("#", end="")
            if i != n - 1:
                print()
        print()
