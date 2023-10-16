#!/usr/bin/python3
""" This module contains the base class for all other classes in thid project
"""
import json


class Base:
    """
        This class will be the “base” of all other classes in this project.

    The goal of it is to manage id attribute in all the future classes
    and to avoid duplicating the same code

    private class attribute
    ------------------------
            __nb_objects = 0

    class constructor
    -----------------
            def __init__(self, id=None)

    public instance attribute
    -------------------------
            id : int

    static methods
    --------------
        def to_json_string(list_dictionaries):
             returns the JSON string representation of list_dictionaries

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        The object constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        obj = None
        if cls.__name__ == "Rectangle":
            obj = cls(2, 3)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        new_list = []
        try:
            with open(file_name, "r") as f:
                json_string = f.read()
            list_objects = Base.from_json_string(json_string)
            for obj_dict in list_objects:
                new_list.append(cls.create(**obj_dict))

            return new_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""

        file_name = cls.__name__ + ".csv"
        with open(file_name, "w") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        file_name = cls.__name__ + ".csv"
        new_list = []
        try:
            with open(file_name, "r") as f:
                json_string = f.read()
            list_objects = Base.from_json_string(json_string)
            for obj_dict in list_objects:
                new_list.append(cls.create(**obj_dict))

            return new_list
        except FileNotFoundError:
            return []
