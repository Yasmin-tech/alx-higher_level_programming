#!/usr/bin/python3
"""
        This module contains the Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base.

    This class defines a rectangle object

    class constructor
    -----------------
        def __init__(self, width, height, x=0, y=0, id=None)
        call the __init__(id) of the base class

    private instance attributes
    -------------------------
        id : int
        width : int
        height : int
        x : int
        y : int

    public instance methods
    -------------------------

        getter / setter: def width (self)
        getter / setter: def height (self)
        getter / setter: def x (self)
        getter / setter: def y (self)

        def area(self):
                calculate and returns the area value of the Rectangle instance
        def display(self):
                prints in stdout the Rectangle instance with the character #

        def __str__(self) -> str:
                Return str represintation:
                [Rectangle] (<id>) <x>/<y> - <width>/<height>

        def to_dictionary(self):
                returns the dictionary representation of a Rectangle

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Construct the object
        call the __init__(id) of the base class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate and returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        taking care of x and y;
            print spaces before # numbers of x
            print new lines before # numbers of y
        """
        column = self.width
        rows = self.height
        # print new lines
        print("\n" * self.y, end="")
        for _ in range(rows):
            print(" " * self.x + "#" * column)

    def __str__(self) -> str:
        """Return str represintation
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Update the Rectangle by assigns an argument to each attribute:

        args* - no-keyword arguments:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute

        kwargs* - keyworded arguments: keys and values
        """

        attr = [arg for arg in args]

        if len(attr) > 0:
            if attr[0] is None:
                self.__init__(self.width, self.height, self.x, self.y)
            else:
                self.id = attr[0]
        if len(attr) > 1:
            self.width = attr[1]
        if len(attr) > 2:
            self.height = attr[2]
        if len(attr) > 3:
            self.x = attr[3]
        if len(attr) > 4:
            self.y = attr[4]

        if not args or len(args) == 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self) -> dict:
        """that returns the dictionary representation of a Rectangle"""
        obj_dict = {}
        obj_dict["id"] = self.id
        obj_dict["width"] = self.width
        obj_dict["height"] = self.height
        obj_dict["x"] = self.x
        obj_dict["y"] = self.y
        return obj_dict
