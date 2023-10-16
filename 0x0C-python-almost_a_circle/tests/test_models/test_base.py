#!/usr/bin/python3
""" This module contains test cases the base.py
"""
import unittest
import math
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    Define the class for testing the Base class
    """

    def test_init_no_args(self) -> None:
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_init_with_int_args(self) -> None:
        obj1 = Base(12)
        obj2 = Base(14)
        self.assertEqual(obj1.id, 12)
        self.assertEqual(obj2.id, 14)

    def test_init_with_without_args(self) -> None:
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(12)
        obj4 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, obj1.id + 1)
        self.assertEqual(obj3.id, 12)
        self.assertEqual(obj4.id, obj1.id + 2)

    def test_set_id_after_created(self):
        Base._Base__nb_objects = 0
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj1.id = 50
        self.assertEqual(obj1.id, 50)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def test_access_nb_objects_from_obj(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

        self.assertFalse(hasattr(Base(10), "__nb_objects"))

    def test_set_id_none_after_created(self):
        Base._Base__nb_objects = 0
        obj1 = Base()
        self.assertEqual(1, obj1.id)
        obj1.id = None
        self.assertIsNone(obj1.id)

    def test_none_id(self):
        obj1 = Base(None)
        obj2 = Base(None)
        obj3 = Base(None)
        self.assertEqual(obj1.id, obj3.id - 2)

    def test_id_is_public(self):
        obj1 = Base(20)
        obj1.id = 30
        self.assertEqual(obj1.id, 30)

    def test_nb_objects(self):
        Base._Base__nb_objects = 3
        obj1 = Base()
        self.assertEqual(obj1.id, 4)

    def test_init_with_two_args(self):
        with self.assertRaises(TypeError):
            Base(4, 8)

    def test_id_float(self):
        Base._Base__nb_objects = 0
        obj1 = Base(5.5)
        self.assertEqual(obj1.id, 5.5)

        obj2 = Base()
        self.assertEqual(obj2.id, 1)

    def test_id_str(self):
        obj1 = Base("first_obj")
        self.assertEqual(obj1.id, "first_obj")

        obj2 = Base()
        obj3 = Base("Third_obj")
        self.assertEqual(obj3.id, "Third_obj")

        obj4 = Base()
        self.assertEqual(obj2.id, obj4.id - 1)

    def test_id_list(self):
        obj1 = Base([0, 1, 2])
        self.assertEqual(obj1.id, [0, 1, 2])

        obj2 = Base()
        obj3 = Base([3, 4, 5])
        self.assertEqual(obj3.id, [3, 4, 5])

        obj4 = Base()
        self.assertEqual(obj4.id, obj2.id + 1)

    def test_id_dict(self):
        self.assertEqual({1, 2, 3.4}, Base({1, 2, 3.4}).id)

    def test_id_inf(self):
        self.assertEqual(float("inf"), Base(float("inf")).id)

    def test_id_tuple(self):
        self.assertEqual((1, 2, 3.4), Base((1, 2, 3.4)).id)

    def test_id_NaN(self):
        self.assertTrue(math.isnan(Base(float("inf") - float("inf")).id))


if __name__ == "__main__":
    unittest.main()
