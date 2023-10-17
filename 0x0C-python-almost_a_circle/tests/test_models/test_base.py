#!/usr/bin/python3
""" This module contains test cases the base.py
"""
import unittest
import math
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """
    Define the class for testing the Base class
    """

    def test_init_no_args(self) -> None:
        """test init with no args"""
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


class TestStaticMethod_to_json_string(unittest.TestCase):
    """Test the static mthod to_json_string"""

    def test_to_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_empty_tuple(self):
        self.assertEqual("[]", Base.to_json_string(()))

    def test_with_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_with_one_rectangle_object(self):
        Base._Base__nb_objects = 0
        r = Rectangle(1, 2)
        r_dict = r.to_dictionary()
        excepted_output = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
        self.assertEqual(excepted_output, Base.to_json_string([r_dict]))

    def test_to_json_string_return(self):
        Base._Base__nb_objects = 0
        r = Rectangle(1, 2)
        r_dict = r.to_dictionary()
        excepted_output = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
        self.assertEqual(str, type(Base.to_json_string([r_dict])))

    def test_with_rectangle_two_object(self):
        Base._Base__nb_objects = 0
        r = Rectangle(1, 2)
        r_dict = r.to_dictionary()
        r1 = Rectangle(3, 4)
        r_dict1 = r1.to_dictionary()
        excepted_output = (
            '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, '
            '{"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}]'
        )
        self.assertEqual(excepted_output, Base.to_json_string([r_dict, r_dict1]))

    def test_with_one_square_object(self):
        Base._Base__nb_objects = 0
        s = Square(1)
        s_dict = s.to_dictionary()
        excepted_output = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        self.assertEqual(excepted_output, Base.to_json_string([s_dict]))

    def test_with_two_square_object(self):
        Base._Base__nb_objects = 0
        s = Square(2)
        s_dict = s.to_dictionary()
        s2 = Square(4)
        s2_dict = s2.to_dictionary()
        excepted_output = (
            '[{"id": 1, "size": 2, "x": 0, "y": 0}, '
            '{"id": 2, "size": 4, "x": 0, "y": 0}]'
        )
        self.assertEqual(excepted_output, Base.to_json_string([s_dict, s2_dict]))


class TestBase_save_to_file(unittest.TestCase):
    """Testing save_to_file method"""

    def test_save_to_file_no_args(self):
        r = Rectangle(5, 7)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_with_two_args(self):
        r = Rectangle(5, 7)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(Rectangle, [r])

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            string = f.read()
        self.assertEqual(string, "[]")

    def test_save_to_file_with_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            string = f.read()
        self.assertEqual(string, "[]")

    def test_save_to_file_one_rectangle_object(self):
        r = Rectangle(5, 7, id=10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            string = f.read()
        self.assertEqual(
            string, '[{"id": 10, "width": 5, "height": 7, "x": 0, "y": 0}]'
        )

    def test_save_to_file_two_rectangle_object(self):
        r = Rectangle(5, 7, id=10)
        r1 = Rectangle(6, 8, id=20)
        Rectangle.save_to_file([r, r1])
        with open("Rectangle.json", "r") as f:
            string = f.read()
        self.assertEqual(
            string,
            '[{"id": 10, "width": 5, "height": 7, "x": 0, "y": 0}, '
            '{"id": 20, "width": 6, "height": 8, "x": 0, "y": 0}]',
        )

    def test_save_to_file_one_square_object(self):
        s = Square(5, id=10)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            string = f.read()
        self.assertEqual(string, '[{"id": 10, "size": 5, "x": 0, "y": 0}]')

    def test_save_to_file_two_square_object(self):
        s = Square(5, id=10)
        s1 = Square(6, id=20)
        Square.save_to_file([s, s1])
        with open("Square.json", "r") as f:
            string = f.read()
        self.assertEqual(
            string,
            '[{"id": 10, "size": 5, "x": 0, "y": 0}, '
            '{"id": 20, "size": 6, "x": 0, "y": 0}]',
        )

    def test_save_rectange_square_in_Base_json(self):
        s = Square(5, id=10)
        r = Rectangle(5, 7, id=20)
        Base.save_to_file([s, r])
        with open("Base.json", "r") as f:
            string = f.read()
        self.assertEqual(
            string,
            '[{"id": 10, "size": 5, "x": 0, "y": 0}, '
            '{"id": 20, "width": 5, "height": 7, "x": 0, "y": 0}]',
        )

    def test_the_file_overwriten(self):
        s = Square(5, id=10)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            string = f.read()
        self.assertEqual(string, '[{"id": 10, "size": 5, "x": 0, "y": 0}]')
        s1 = Square(6, id=20)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            string = f.read()
        self.assertEqual(
            string,
            '[{"id": 20, "size": 6, "x": 0, "y": 0}]',
        )


class TestBase_from_json_string(unittest.TestCase):
    """Test from_json_string method"""

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    def test_from_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string("[]", "[]")

    def test_string_of_empty_list(self):
        self.assertEqual([], Rectangle.from_json_string("[]"))

    def test_from_json_string_with_none(self):
        self.assertEqual([], Rectangle.from_json_string(None))

    def test_from_json_string_return_type(self):
        r = Rectangle(1, 2)
        r_json_string = r.to_json_string([r.to_dictionary()])
        self.assertEqual(list, type(Rectangle.from_json_string(r_json_string)))

    def test_list_dicts_one_rectangle(self):
        r = Rectangle(1, 2, id=2)
        r_json_string = r.to_json_string([r.to_dictionary()])
        self.assertEqual(
            [{"id": 2, "width": 1, "height": 2, "x": 0, "y": 0}],
            Rectangle.from_json_string(r_json_string),
        )

    def test_list_dicts_two_rectangle(self):
        r = Rectangle(1, 2, id=2)
        r1 = Rectangle(5, 7, id=10)
        json_string = Base.to_json_string([r.to_dictionary(), r1.to_dictionary()])
        self.assertEqual(
            [
                {"id": 2, "width": 1, "height": 2, "x": 0, "y": 0},
                {"id": 10, "width": 5, "height": 7, "x": 0, "y": 0},
            ],
            Rectangle.from_json_string(json_string),
        )

    def test_list_dicts_one_square(self):
        s = Square(2, id=2)
        s_json_string = s.to_json_string([s.to_dictionary()])
        self.assertEqual(
            [{"id": 2, "size": 2, "x": 0, "y": 0}],
            Rectangle.from_json_string(s_json_string),
        )

    def test_list_dicts_two_square(self):
        s = Square(2, id=2)
        s1 = Square(7, id=10)
        json_string = Base.to_json_string([s.to_dictionary(), s1.to_dictionary()])
        self.assertEqual(
            [
                {"id": 2, "size": 2, "x": 0, "y": 0},
                {"id": 10, "size": 7, "x": 0, "y": 0},
            ],
            Rectangle.from_json_string(json_string),
        )

    def test_list_dicts_square_rectangle(self):
        s = Square(2, id=2)
        r = Rectangle(5, 7, id=10)
        json_string = Base.to_json_string([s.to_dictionary(), r.to_dictionary()])
        self.assertEqual(
            [
                {"id": 2, "size": 2, "x": 0, "y": 0},
                {"id": 10, "width": 5, "height": 7, "x": 0, "y": 0},
            ],
            Rectangle.from_json_string(json_string),
        )


class TestBase_create(unittest.TestCase):
    """Test create method"""

    def test_create_rectangle_no_args(self):
        # return the dummy object
        self.assertEqual(type(Rectangle.create()), Rectangle)

    def test_create_square_no_args(self):
        # return the dummy object
        self.assertEqual(type(Square.create()), Square)

    def test_create_possitional_args(self):
        with self.assertRaises(TypeError):
            self.assertEqual(type(Rectangle.create(None)), Rectangle)

    def test_create_from_rectangle_dict(self):
        r = Rectangle(1, 2)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertEqual(str(r), str(r2))

    def test_create_from_rectangle_dict_checkoutput(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r2))

    def test_create_new_dict_checkoutput(self):
        r2 = Rectangle.create(id=5, x=3, width=1, y=4, height=2)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(r2))

    def test_create_from_rectangle_dict_is(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertIsNot(r, r2)

    def test_create_from_rectangle_dict_is(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertNotEqual(r, r2)

    def test_create_from_square_dict(self):
        s = Square(1)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertEqual(str(s), str(s2))

    def test_create_from_square_dict_checkoutput(self):
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertEqual("[Square] (5) 3/4 - 2", str(s2))

    def test_create_new_square_dict_checkoutput(self):
        s = Square.create(id=5, x=3, size=1, y=4)
        self.assertEqual("[Square] (5) 3/4 - 1", str(s))

    def test_create_from_rectangle_dict_is(self):
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertIsNot(s, s2)

    def test_create_from_rectangle_dict_is(self):
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertNotEqual(s, s2)


# class TestBase_load_from_file(unittest.TestCase):
#     """Test load_from_file_method o"""

#     def test_load_from_file_rectangleone(self):
#         r1 = Rectangle(10, 9, 0, 0, 1)
#         r2 = Rectangle(2, 5, 7, 8, 9)
#         Rectangle.save_to_file([r1, r2])
#         list_rectangles_output = Rectangle.load_from_file()
#         self.assertEqual(str(r1), str(list_rectangles_output[0]))

#     def test_load_from_file_rectangle_two(self):
#         r1 = Rectangle(10, 9, 0, 0, 1)
#         r2 = Rectangle(2, 5, 7, 8, 9)
#         Rectangle.save_to_file([r1, r2])
#         list_rectangles_output = Rectangle.load_from_file()
#         self.assertEqual(str(r2), str(list_rectangles_output[1]))

#     def test_load_from_file_types_rectangle(self):
#         r1 = Rectangle(10, 9, 0, 0, 1)
#         r2 = Rectangle(2, 5, 7, 8, 9)
#         Rectangle.save_to_file([r1, r2])
#         output = Rectangle.load_from_file()
#         self.assertTrue(all(type(obj) == Rectangle for obj in output))

#     def test_load_from_file_square_one(self):
#         s1 = Square(5, 1, 8, 3)
#         s2 = Square(9, 5, 2, 3)
#         Square.save_to_file([s1, s2])
#         list_squares_output = Square.load_from_file()
#         self.assertEqual(str(s1), str(list_squares_output[0]))

#     def test_load_from_file_square_two(self):
#         s1 = Square(5, 1, 8, 3)
#         s2 = Square(9, 5, 2, 3)
#         Square.save_to_file([s1, s2])
#         list_squares_output = Square.load_from_file()
#         self.assertEqual(str(s2), str(list_squares_output[1]))

#     def test_load_from_file_types_square(self):
#         s1 = Square(5, 1, 8, 3)
#         s2 = Square(9, 5, 2, 3)
#         Square.save_to_file([s1, s2])
#         output = Square.load_from_file()
#         self.assertTrue(all(type(obj) == Square for obj in output))

#     def test_load_from_file_no_file(self):
#         output = Base.load_from_file()
#         self.assertEqual([], output)

#     def test_load_from_file_more_than_one_arg(self):
#         with self.assertRaises(TypeError):
#             Base.load_from_file([], 1)
