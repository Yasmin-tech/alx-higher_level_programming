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

    number_of_instances = 0
    print_symbol = "#"

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

        type(self).number_of_instances += 1

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

    def area(self):
        """ A function that calculates and returns the rectangle area

        Args
        ----
                self: the object
        """
        return self.__width * self.__height

    def perimeter(self):
        """ A function that calculates and returns the rectangle perimeter

        Args
        ----
                self: the object
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self) -> str:
        """ return a string representation of rectangle with the
        character stored in print_symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        string = []
        for i in range(self.__height):
            for j in range(self.__width):
                string.append(str(self.print_symbol))
            if i != self.__height - 1:
                string.append("\n")

        return "".join(string)

    def __repr__(self) -> str:
        """ return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle(" + str(self.__width) + ", " +\
            str(self.__height) + ")"

    def __del__(self):
        """ Delete the object self. """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a_rect_1 = rect_1.area()
        a_rect_2 = rect_2.area()

        if a_rect_1 >= a_rect_2:
            return rect_1

        return rect_2
