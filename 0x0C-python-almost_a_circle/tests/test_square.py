""" This module contains test cases the square.py
"""
import unittest
import contextlib
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestInstantiation_Square(unittest.TestCase):
    """Test if an object of Square has been created correctly"""

    def test_inheritance(self):
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertIsInstance(Square(1), Base)
        self.assertIsInstance(Square(1), Base)

    def test_instantiation_with_no_args(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_instanse_attr(self):
        s = Square(5)
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "width"))
        self.assertTrue(hasattr(s, "height"))
        self.assertTrue(hasattr(s, "x"))
        self.assertTrue(hasattr(s, "y"))
        self.assertTrue(hasattr(s, "size"))

    def test_instantiation_with_one_required_size_arg(self):
        s = Square(5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.size, 5)

    def test_instantiation_with_only_id(self):
        with self.assertRaises(TypeError):
            s = Square(id=2)

    def test_instantiation_with_id_and_size(self):
        s = Square(6, id=20)
        self.assertEqual(6, s.size)
        self.assertEqual(20, s.id)

    def test_instantiation_with_id_equal_None_and_size(self):
        Base._Base__nb_objects = 0
        s = Square(6, id=None)
        self.assertEqual(6, s.size)
        self.assertEqual(1, s.id)

    def test_id_suare_after_rectangle_instantiation(self):
        Base._Base__nb_objects = 0
        r = Rectangle(9, 6)
        s = Square(8)
        self.assertEqual(s.id - 1, r.id)

    def test_instantiation_with_id_x_and_y(self):
        with self.assertRaises(TypeError):
            s = Square(x=0, y=0, id=12)

    def test_instantiation_with_three_args(self):
        s1 = Square(10, 20, 6)
        s2 = Square(9, 9, 8)
        self.assertEqual(s2.id, s1.id + 1)

    def test_instantiation_with_four_args(self):
        s1 = Square(10, 20, 6, 7)
        s2 = Square(9, 9, 8, 8)
        self.assertEqual(s1.id, 7)
        self.assertEqual(s2.id, 8)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_access_private_width(self):
        with self.assertRaises(AttributeError):
            print(Square(9).__width)

        s1 = Square(5, 6)
        s1.__width = 10
        self.assertEqual(10, s1.__width)

    def test_access_private_height(self):
        with self.assertRaises(AttributeError):
            print(Square(10).__height)

        s1 = Square(5)
        s1.__height = 10
        self.assertEqual(10, s1.__height)

    def test_access_private_x(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 1, 1, 1).__x)

    def test_access_private_y(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 1, 1, 1).__y)

    def test_access_private_size(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 1, 1, 1).__size)

    def test_create_dynamic_attr(self):
        s1 = Square(6)
        s1.area = None
        self.assertTrue(hasattr(s1, "area"))

    def test_get_size_width_height(self):
        s1 = Square(20, 6, 7, 16)
        self.assertEqual(20, s1.size)
        self.assertEqual(20, s1.width)
        self.assertEqual(20, s1.height)

    def test_get_size_width_height_after_change_width(self):
        s1 = Square(20, 6, 7, 16)
        s1.width = 3
        self.assertEqual(3, s1.size)
        self.assertEqual(3, s1.width)
        self.assertEqual(20, s1.height)

    def test_get_size_width_height_after_change_height(self):
        s1 = Square(20, 6, 7, 16)
        s1.height = 11
        self.assertEqual(20, s1.size)
        self.assertEqual(20, s1.width)
        self.assertEqual(11, s1.height)

    def test_get_size_width_height_after_change_size(self):
        s1 = Square(20, 6, 7, 16)
        s1.size = 110
        self.assertEqual(110, s1.size)
        self.assertEqual(110, s1.width)
        self.assertEqual(110, s1.height)

    def test_get_defult_x_and_y(self):
        s1 = Square(20)
        self.assertEqual(0, s1.x)
        self.assertEqual(0, s1.x)

    def test_get_x(self):
        s1 = Square(20, 6, 7, 16)
        self.assertEqual(6, s1.x)

    def test_set_x(self):
        s1 = Square(20, 6, 7, 16)
        s1.x = 2
        self.assertEqual(2, s1.x)

    def test_get_y(self):
        s1 = Square(20, 6, 7, 16)
        self.assertEqual(7, s1.y)

    def test_set_y(self):
        s1 = Square(20, 6, 7, 16)
        s1.y = 2
        self.assertEqual(2, s1.y)


class TestValidation_size_attr(unittest.TestCase):
    """
    Test if the values of attribute "size" of Square object are valid
    """

    def test_size_float(self):
        with self.assertRaises(TypeError) as err:
            Square(5.8)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_str(self):
        with self.assertRaises(TypeError) as err:
            Square("2")
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_bool(self):
        with self.assertRaises(TypeError) as err:
            Square(True)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_list(self):
        with self.assertRaises(TypeError) as err:
            Square([4])
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_dict(self):
        with self.assertRaises(TypeError) as err:
            Square({"width": 4})
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_set(self):
        with self.assertRaises(TypeError) as err:
            Square({1, 4})
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_none(self):
        with self.assertRaises(TypeError) as err:
            Square(None)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_nan(self):
        with self.assertRaises(TypeError) as err:
            Square(float("nan"))
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_inf(self):
        with self.assertRaises(TypeError) as err:
            Square(float("inf"))
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_range(self):
        with self.assertRaises(TypeError) as err:
            Square(range(3))
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_valu_zero(self):
        with self.assertRaises(ValueError) as err:
            Square(0)
        self.assertEqual("width must be > 0", str(err.exception))

    def test_complex_size(self):
        with self.assertRaises(TypeError) as err:
            Square(complex(3))
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_frozenset(self):
        with self.assertRaises(TypeError) as err:
            Square(frozenset({1, 2, 3}))
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_tuple(self):
        with self.assertRaises(TypeError) as err:
            Square((1,))
        self.assertEqual("width must be an integer", str(err.exception))

    def test_size_valu_negative_zero(self):
        with self.assertRaises(ValueError) as err:
            Square(-0)
        self.assertEqual("width must be > 0", str(err.exception))

    def test_size_valu_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(-1)
        self.assertEqual("width must be > 0", str(err.exception))


class TestValidation_x_attr(unittest.TestCase):
    """
    Test if the values of attribute "x" of Square object are valid
    """

    def test_x_float(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 2.2)
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_str(self):
        with self.assertRaises(TypeError) as err:
            Square(5, "2")
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_bool(self):
        with self.assertRaises(TypeError) as err:
            Square(5, True)
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_list(self):
        with self.assertRaises(TypeError) as err:
            Square(5, [9])
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_dict(self):
        with self.assertRaises(TypeError) as err:
            Square(5, {"width": 4})
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_set(self):
        with self.assertRaises(TypeError) as err:
            Square(5, {1, 4})
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_none(self):
        with self.assertRaises(TypeError) as err:
            Square(5, None)
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_nan(self):
        with self.assertRaises(TypeError) as err:
            Square(5, float("nan"))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_inf(self):
        with self.assertRaises(TypeError) as err:
            Square(5, float("inf"))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_range(self):
        with self.assertRaises(TypeError) as err:
            Square(5, range(3))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_valu_zero(self):
        self.assertEqual(0, Square(5, 0).x)

    def test_complex_x(self):
        with self.assertRaises(TypeError) as err:
            Square(5, complex(3))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_frozenset(self):
        with self.assertRaises(TypeError) as err:
            Square(7, frozenset({1, 2, 3}))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_tuple(self):
        with self.assertRaises(TypeError) as err:
            Square(4, (1,))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_valu_negative_zero(self):
        self.assertEqual(0, Square(8, -0).x)

    def test_x_valu_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(7, -1)
        self.assertEqual("x must be >= 0", str(err.exception))


class TestValidation_y_attr(unittest.TestCase):
    """
    Test if the values of attribute "y" of Square object are valid
    """

    def test_valid_y(self):
        self.assertEqual(Square(2, 4, 8).y, 8)

    def test_y_float(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, 2.2)
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_str(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, "2")
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_bool(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, True)
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_list(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, [9])
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_dict(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, {"width": 4})
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_set(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, {1, 4})
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_none(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, None)
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_nan(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 3, float("nan"))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_inf(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 4, float("inf"))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_range(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 4, range(3))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_valu_zero(self):
        self.assertEqual(0, Square(5, 8, 0).y)

    def test_complex_y(self):
        with self.assertRaises(TypeError) as err:
            Square(5, 8, complex(3))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_x_frozenset(self):
        with self.assertRaises(TypeError) as err:
            Square(7, 8, frozenset({1, 2, 3}))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_tuple(self):
        with self.assertRaises(TypeError) as err:
            Square(4, 5, (1,))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_valu_negative_zero(self):
        self.assertEqual(0, Square(8, 5, -0).y)

    def test_y_valu_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(7, 5, -1)
        self.assertEqual("y must be >= 0", str(err.exception))


class TestSquare_initialization_oreder(unittest.TestCase):
    """Testing order of Square initialization"""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("3", (2,))

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, (9,), (8,))

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({6}, 10, "9")


class TestAreaMethod(unittest.TestCase):
    """area() is an instance method in the Rectangle object that is
    inherited by Square.
    """

    def test_area_attr(self):
        s = Square(8)
        self.assertTrue(hasattr(s, "area"))

    def test_area_args(self):
        s = Square(9)
        with self.assertRaises(TypeError) as err:
            area = s.area(s)
        self.assertEqual(
            "Rectangle.area() takes 1 positional argument but 2 were given",
            str(err.exception),
        )

    def test_area_assiging(self):
        s = Square(9)
        s.area = 70
        with self.assertRaises(TypeError) as err:
            self.assertEqual(72, s.area())
        self.assertEqual("'int' object is not callable", str(err.exception))

    def test_squareArea_with_two_args(self):
        self.assertEqual(16, Square(4).area())

    def test_squareArea_with_three_args(self):
        self.assertEqual(9, Square(3, 5, 3).area())

    def test_squareArea_four_three_args(self):
        self.assertEqual(100, Square(10, 50, 3, 0).area())

    def test_squareArea_after_size_change(self):
        s = Square(10, 10, 3, 0)
        s.size = 6
        self.assertEqual(36, s.area())

    def test_squareArea_after_height_change(self):
        s = Square(3, 1, 3, 0)
        s.height = 7
        self.assertEqual(21, s.area())

    def test_squareArea_after_width_change(self):
        s = Square(3, 1, 3, 0)
        s.width = 7
        self.assertEqual(21, s.area())

    def test_SquareArea_change_x(self):
        s = Square(2, 1, 3, 0)
        self.assertEqual(4, s.area())
        s.x = 1
        self.assertEqual(4, s.area())

    def test_SquareArea_change_y(self):
        s = Square(2, 1, 3, 0)
        self.assertEqual(4, s.area())
        s.y = 1
        self.assertEqual(4, s.area())

    def test_BigSquareArea(self):
        s = Square(999999999999, 1, 3, 0)
        self.assertEqual(999999999998000000000001, s.area())


class Test_display_stdout(unittest.TestCase):
    """Test if display prints # in stdout"""

    def test_display_attr(self):
        self.assertTrue(hasattr(Square(2), "display"))

    def test_display_args(self):
        s = Square(9)
        with self.assertRaises(TypeError) as err:
            s.display("#")
        self.assertEqual(
            "Rectangle.display() takes 1 positional argument but 2 were given",
            str(err.exception),
        )

        #     # Redirect stdout to a string buffer
        #     @staticmethod
        #     def check_stdout(rect, method):
        #         buffer = io.StringIO
        #         sys.stdout = buffer
        #         if method == "display":
        #             rect.display()
        #         sys.stdout = sys.__stdout__
        #         return buffer

        #     def test_display_output(self):
        #         rect1 = Rectangle(2, 3)
        #         stdout_buffer =
        #         Test_print_stdout.check_stdout(rect1, "display")
        #         self.assertEqual(stdout_buffer.getvalue(), "##\n##\n##\n")

    def test_display_with_size(self):
        # Create a rectangle and call display
        s = Square(3)
        # Use context manager to temporarily redirect stdout
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        # Check if the output is correct
        self.assertEqual(output, "###\n###\n")

    def test_display_with_size(self):
        # Create a rectangle and call display
        s = Square(1)
        # Use context manager to temporarily redirect stdout
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        # Check if the output is correct
        self.assertEqual(output, "#\n")

    def test_display_with_x_y_zero(self):
        s = Square(4, 0, 0)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        self.assertEqual(output, "####\n####\n####\n####\n")

    def test_display_with_x(self):
        s = Square(5, 3)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        self.assertEqual(output, "   #####\n" * 5)

    def test_display_with_y(self):
        s = Square(6, y=3)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n\n\n" + "######\n" * 6)

    def test_display_with_x_equal_y(self):
        s = Square(6, 8, 8)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n\n\n\n\n\n\n\n" + "        ######\n" * 6)

    def test_display_with_x_notequal_y(self):
        s = Square(2, 2, 3)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n\n\n" + "  ##\n" * 2)

    def test_display_with_x_y_equal_one(self):
        r1 = Rectangle(1, 1, 1, 1)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n" + " #\n")


class TestSquare_ptint_str(unittest.TestCase):
    """test __str__ method"""

    def test_str_size(self):
        Base._Base__nb_objects = 0
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(Square(9))
            stdout_output = buf.getvalue()
        expected_output = "[Square] (1) 0/0 - 9\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_size_directAccess(self):
        Base._Base__nb_objects = 0
        s = Square(9)
        expected_output = "[Square] (1) 0/0 - 9"
        self.assertEqual(expected_output, s.__str__())
        self.assertEqual(expected_output, str(s))

    def test_str_args(self):
        with self.assertRaises(TypeError):
            s = Square(8)
            s.__str__(s)

    def test_str_size_and_id(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(Square(8, 0, 0, 100))
            stdout_output = buf.getvalue()
        expected_output = "[Square] (100) 0/0 - 8\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_size_and_id_and_x(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(Square(8, 6, id=100))
            stdout_output = buf.getvalue()
        expected_output = "[Square] (100) 6/0 - 8\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_width_height_id_x_y(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(Square(8, 5, 6, 100))
            stdout_output = buf.getvalue()
        expected_output = "[Square] (100) 5/6 - 8\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_size_changed(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s = Square(9, 7, 9, 100)
            s.size = 3
            print(s)
            stdout_output = buf.getvalue()
        expected_output = "[Square] (100) 7/9 - 3\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_id_changed(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s = Square(9, 7, 9, 100)
            s.id = 99
            print(s)
            stdout_output = buf.getvalue()
        expected_output = "[Square] (99) 7/9 - 9\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_x_y_changed(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s = Square(2, 7, 9, 0)
            s.x = 0
            s.y = 0
            print(s)
            stdout_output = buf.getvalue()
        expected_output = "[Square] (0) 0/0 - 2\n"
        self.assertEqual(expected_output, stdout_output)


class TestSquare_update(unittest.TestCase):
    """Test the Rectangle update method"""

    def test_update_attr(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertTrue(hasattr(s, "update"))

    def test_update_one_arg(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")

    def test_update_two_arg(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")

        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 2")

    def test_update_two_valid_arg(self):
        s = Square(10, 10, 10)
        with self.assertRaises(TypeError) as err:
            s.update(89, 2.2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_update_three_arg(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/10 - 2")

    def test_update_three_valid_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError) as err:
            s.update(89, 2, "3")
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_update_four_arg(self):
        s = Square(10, 10, 10, 10)

        s.update(89, 2, 3, 9)
        self.assertEqual(str(s), "[Square] (89) 3/9 - 2")

    def test_update_four_valid_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError) as err:
            s.update(89, 2, 3, "9")
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_update_more_than_five_arg(self):
        s = Square(10, 10, 10, 10)

        s.update(89, 2, 3, 9, 1, 1, 1, 1)
        self.assertEqual(str(s), "[Square] (89) 3/9 - 2")

    def test_update_no_args_kwargs(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10, 10)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")
        s.update()
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")

    def test_update_none(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10, 10)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")
        s.update(None)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")

    def test_skip_kwargd_one_arg(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")
        s.update(98, size=3)
        self.assertEqual(str(s), "[Square] (98) 10/10 - 10")

    def test_skip_kwargd_two_arg(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")
        s.update(98, 4, size=3, x=1)
        self.assertEqual(str(s), "[Square] (98) 10/10 - 4")

    def test_skip_kwargd_when_args_None(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")
        s.update(None, size=3, x=1)
        self.assertEqual(str(s), "[Square] (2) 10/10 - 10")

    def test_kwargd_with_id_None(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 10")
        s.update(id=None)
        self.assertEqual(str(s), "[Square] (2) 10/10 - 10")

    def test_kwargd_with_id(self):
        s = Square(10, 10, 10)
        s.update(id=50)
        self.assertEqual(str(s), "[Square] (50) 10/10 - 10")

    def test_kwargd_size(self):
        s = Square(10, 10, 10)
        s.id = 1
        s.update(size=3)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 3")

    def test_kwargd_size_updates_width_height(self):
        s = Square(10, 10, 10, 1)
        s.update(size=3)
        self.assertEqual(3, s.width)
        self.assertEqual(3, s.height)
        self.assertEqual(3, s.size)

    def test_kwargd_ordered(self):
        s = Square(10)
        s.update(id=50, size=3, x=1, y=1)
        self.assertEqual(str(s), "[Square] (50) 1/1 - 3")

    def test_kwargd_inreverse(self):
        s = Square(10)
        s.update(y=1, size=3, id=50)
        self.assertEqual(str(s), "[Square] (50) 0/1 - 3")

    def test_kwargd_two_orderedkeys(self):
        Base._Base__nb_objects = 0
        s = Square(10)
        s.update(id=None, size=3)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 3")

    def test_kwargd_two_unorderedkeys(self):
        Base._Base__nb_objects = 0
        s = Square(10)
        s.update(size=3, id=None)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 3")

    def test_kwargd_three_unorderedkeys(self):
        Base._Base__nb_objects = 0
        s = Square(10)
        s.update(id=None, y=2, size=3)
        self.assertEqual(str(s), "[Square] (2) 0/2 - 3")

    def test_kwargd_three_orderedkeys(self):
        Base._Base__nb_objects = 0
        s = Square(10)
        s.update(id=98, size=3, x=10)
        self.assertEqual(str(s), "[Square] (98) 10/0 - 3")

    def test_kwargd_four_unorderedkeys(self):
        Base._Base__nb_objects = 0
        s = Square(10)
        s.update(size=4, x=6, id=7, y=0)
        self.assertEqual(str(s), "[Square] (7) 6/0 - 4")

    def test_kwargd_not_changing_values(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10, 10)
        s.update(height=10, id=10, x=10, width=10, y=10)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")

    def test_kwargd_key_not_exsit(self):
        Base._Base__nb_objects = 0
        s = Square(10, 10, 10, 10)
        s.update(h=10)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")


class TestSquare_to_dictionary(unittest.TestCase):
    """Test to_dictionary method"""

    def test_to_dictionary_args(self):
        with self.assertRaises(TypeError):
            Square(9).to_dictionary("dict")

    def test_toDictionary_output(self):
        Base._Base__nb_objects = 0
        s = Square(8)
        excepted_output = {"id": 1, "size": 8, "x": 0, "y": 0}
        # self.assertEqual(r.to_dictionary(), excepted_output)
        self.assertDictEqual(s.to_dictionary(), excepted_output)

    def test_toDictionary_output_after_set_attributes(self):
        Base._Base__nb_objects = 0
        s = Square(8)
        s.id = 10
        s.x = 1
        s.y = 9
        excepted_output = {"id": 10, "size": 8, "x": 1, "y": 9}
        # self.assertEqual(r.to_dictionary(), excepted_output)
        self.assertDictEqual(s.to_dictionary(), excepted_output)

    def test_update_object_with_toDictionary(self):
        s = Square(9)
        s2 = Square(2)
        self.assertNotEqual(s, s2.update(**s.to_dictionary()))


if __name__ == "__main__":
    unittest.main()
