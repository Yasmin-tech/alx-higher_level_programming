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
    def position(self, value):
        """ a setter method for position attribute. """

        if not isinstance(value, tuple)\
                or len(value) != 2\
                or not isinstance(value[0], int)\
                or not isinstance(value[1], int)\
                or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ a method that returns the current square area. """

        return self.__size * self.__size

    def my_print(self):
        """ prints the square in # to stdout. """
        n = self.__size
        if n == 0:
            print()
            return
        spaces = self.__position[0]
        for line in range(self.__position[1]):
            print()
        for i in range(n):
            for k in range(spaces):
                print(" ", end="")
            for j in range(n):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns a string representation of the square. """
        n = self.__size
        if n == 0:
            return
        square_list = []
        for line in range(self.__position[1]):
            square_list.append("\n")
        for i in range(n):
            for space in range(self.__position[0]):
                square_list.append(" ")
            for j in range(n):
                square_list.append("#")
            if i != n - 1:
                square_list.append("\n")
        return "".join(square_list)
