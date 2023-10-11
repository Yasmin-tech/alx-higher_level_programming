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
        if attrs is None or not attrs:
            return self.__dict__

        if type(attrs) is not list:
            return self.__dict__
        if not all(isinstance(item, str) for item in attrs):
            return self.__dict__

        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
