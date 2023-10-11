#!/usr/bin/python3
""" The module of Student class
"""


class Student:
    """a class Student that defines a student

    Public instance attributes
    --------------------------

            first_name : str
            last_name  : str
            age : int

            Public method def to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """initialize an object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs == None or not attrs:
            return self.__dict__

        filter_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                filter_dict[key] = value
        return filter_dict
