#!/usr/bin/python3
"""
        This module contains the Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square object. it inherits from Rectangle

    it doesn't create new attributes, but it uses
    all attributes and motheds of parent

    The overloading __str__ method should return:
            [Square] (<id>) <x>/<y> - <size>

    def to_dictionary(self):
                returns the dictionary representation of a Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Construct a square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """a getter method to the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """A setter to with and highr i.e size of the square"""
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """Square Object string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the Rectangle by assigns an argument to each attribute:

        args* - no-keyword arguments:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3th argument should be the x attribute
        4th argument should be the y attribute

        kwargs* - keyworded arguments: keys and values
        """

        attr = [arg for arg in args]

        if len(attr) > 0:
            if attr[0] is None:
                self.__init__(self.size, self.x, self.y)
            else:
                self.id = attr[0]
        if len(attr) > 1:
            self.size = attr[1]
        if len(attr) > 2:
            self.x = attr[2]
        if len(attr) > 3:
            self.y = attr[3]

        if not args or len(args) == 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self) -> dict:
        """that returns the dictionary representation of a Square"""
        obj_dict = {}
        obj_dict["id"] = self.id
        obj_dict["size"] = self.size
        obj_dict["x"] = self.x
        obj_dict["y"] = self.y
        return obj_dict
