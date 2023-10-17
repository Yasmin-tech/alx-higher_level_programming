""" This module contains test cases the rectangle.py
"""
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle


class TestInstantiation_Rectangle(unittest.TestCase):
    """Test if an object of Rectangle has been created correctly"""

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_instantiation_with_no_args(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle()

    def test_instantiation_with_only_id(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle(id=12)

    def test_instantiation_with_id_x_and_y(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle(x=0, y=0, id=12)

    def test_instantiation_with_two_required_args(self):
        rec1 = Rectangle(10, 20)
        rec2 = Rectangle(10, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_instantiation_with_one_required_args(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle(10, id=20)

    def test_instantiation_with_three_args(self):
        rec1 = Rectangle(10, 20, 6)
        rec2 = Rectangle(9, 9, 8)
        self.assertEqual(rec2.id, rec1.id + 1)

    def test_instantiation_with_four_args(self):
        rec1 = Rectangle(10, 20, 6, 7)
        rec2 = Rectangle(9, 9, 8, 7)
        self.assertEqual(rec2.id, rec1.id + 1)

    def test_instantiation_with_five_args(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        rec2 = Rectangle(9, 9, 8, 7, 15)
        self.assertEqual(rec1.id, 16)
        self.assertEqual(rec2.id, 15)

    def test_access_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(9, 10).__width)

        rec1 = Rectangle(5, 6)
        rec1.__width = 10
        self.assertEqual(10, rec1.__width)

    def test_access_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(9, 10).__height)

        rec1 = Rectangle(5, 6)
        rec1.__height = 10
        self.assertEqual(10, rec1.__height)

    def test_access_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1, 1, 1).__x)

    def test_access_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1, 1, 1).__y)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_create_dynamic_attr(self):
        rec1 = Rectangle(1, 2)
        rec1.area = None
        self.assertTrue(hasattr(rec1, "area"))

    def test_get_width(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        self.assertEqual(10, rec1.width)

    def test_set_width(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        rec1.width = 15
        self.assertEqual(rec1.width, 15)

    def test_get_height(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        self.assertEqual(20, rec1.height)

    def test_set_height(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        rec1.height = 100
        self.assertEqual(rec1.height, 100)

    def test_get_x(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        self.assertEqual(6, rec1.x)

    def test_set_x(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        rec1.x = 9
        self.assertEqual(rec1.x, 9)

    def test_get_y(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        self.assertEqual(7, rec1.y)

    def test_set_y(self):
        rec1 = Rectangle(10, 20, 6, 7, 16)
        rec1.y = 1
        self.assertEqual(rec1.y, 1)


class TestValidation_width_attr(unittest.TestCase):
    """
    Test if the values of attribute "width" of Rectangle object are valid
    """

    def test_width_float(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5.8, 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_str(self):
        with self.assertRaises(TypeError) as err:
            Rectangle("2", 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_bool(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(True, 3)

        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_list(self):
        with self.assertRaises(TypeError) as err:
            Rectangle([4], 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_dict(self):
        with self.assertRaises(TypeError) as err:
            Rectangle({"width": 4}, 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_set(self):
        with self.assertRaises(TypeError) as err:
            Rectangle({1, 4}, 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_none(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(None, 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_nan(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(float("nan"), 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_inf(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(float("inf"), 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_range(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(range(3), 3)
        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_valu_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 3)
        self.assertEqual("width must be > 0", str(err.exception))

    def test_complex_width(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(complex(3), 3)

        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_frozenset(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(frozenset({1, 2, 3}), 3)

        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_tuple(self):
        with self.assertRaises(TypeError) as err:
            Rectangle((1,), 3)

        self.assertEqual("width must be an integer", str(err.exception))

    def test_width_valu_negative_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(-0, 3)
        self.assertEqual("width must be > 0", str(err.exception))

    def test_width_valu_negative(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(-1, 3)
        self.assertEqual("width must be > 0", str(err.exception))


class TestValidation_height_attr(unittest.TestCase):
    """
    Test if the values of attribute "height" of Rectangle object are valid
    """

    def test_height_float(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3.3)
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_str(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, "3")
        self.assertEqual("height must be an integer", str(err.exception))

    def test_width_bool(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, False)

        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_list(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, [3])
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_dict(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, {"width": 4})
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_set(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, {1, 4})
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_none(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, None)
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_nan(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, float("nan"))
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_inf(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, float("inf"))
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_range(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, range(3))
        self.assertEqual("height must be an integer", str(err.exception))

    def test_width_valu_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(5, 0)
        self.assertEqual("height must be > 0", str(err.exception))

    def test_complex_height(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, complex(3))
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_frozenset(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, frozenset({1, 2, 3}))
        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_tuple(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, (1,))

        self.assertEqual("height must be an integer", str(err.exception))

    def test_height_valu_negative_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(5, -0)
        self.assertEqual("height must be > 0", str(err.exception))

    def test_height_valu_negative(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(5, -1)
        self.assertEqual("height must be > 0", str(err.exception))


class TestValidation_x_attr(unittest.TestCase):
    """
    Test if the values of attribute "x" of Rectangle object are valid
    """

    def test_x_float(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 2.2)
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_str(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, "2")
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_bool(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, True)

        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_list(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, [9])
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_dict(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, {"width": 4})
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_set(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, {1, 4})
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_none(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, None)
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_nan(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, float("nan"))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_inf(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 4, float("inf"))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_range(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 4, range(3))
        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_valu_zero(self):
        self.assertEqual(0, Rectangle(5, 8, 0).x)

    def test_complex_x(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 8, complex(3))

        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_frozenset(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(7, 8, frozenset({1, 2, 3}))

        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_tuple(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(4, 5, (1,))

        self.assertEqual("x must be an integer", str(err.exception))

    def test_x_valu_negative_zero(self):
        self.assertEqual(0, Rectangle(8, 5, -0).x)

    def test_x_valu_negative(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(7, 5, -1)
        self.assertEqual("x must be >= 0", str(err.exception))


class TestValidation_y_attr(unittest.TestCase):
    """
    Test if the values of attribute "y" of Rectangle object are valid
    """

    def test_valid_y(self):
        self.assertEqual(Rectangle(1, 2, 4, 8).y, 8)

    def test_y_float(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 9, 2.2)
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_str(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 8, "2")
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_bool(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 77, True)

        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_list(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 6, [9])
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_dict(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 2, {"width": 4})
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_set(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 0, {1, 4})
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_none(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 0, None)
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_nan(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 3, 1, float("nan"))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_inf(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 4, 3, float("inf"))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_range(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 4, 9, range(3))
        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_valu_zero(self):
        self.assertEqual(0, Rectangle(5, 8, 0, 0).y)

    def test_complex_y(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(5, 8, 9, complex(3))

        self.assertEqual("y must be an integer", str(err.exception))

    def test_x_frozenset(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(7, 8, 8, frozenset({1, 2, 3}))

        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_tuple(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(4, 5, 1, (1,))

        self.assertEqual("y must be an integer", str(err.exception))

    def test_y_valu_negative_zero(self):
        self.assertEqual(0, Rectangle(8, 5, 9, -0).y)

    def test_y_valu_negative(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(7, 5, 1, -1)
        self.assertEqual("y must be >= 0", str(err.exception))


class TestAreaMethod(unittest.TestCase):
    """area() is an instance method in the Rectangle object. This

    it uses width and height to calculate the area.
    This class to test the return
    """

    def test_area_attr(self):
        rect = Rectangle(9, 8)
        self.assertTrue(hasattr(rect, "area"))

    def test_area_args(self):
        rect = Rectangle(9, 8)
        with self.assertRaises(TypeError) as err:
            area = rect.area(rect)
        self.assertEqual(
            "Rectangle.area() takes 1 positional argument but 2 were given",
            str(err.exception),
        )

    def test_area_assiging(self):
        rect = Rectangle(9, 8)
        rect.area = 70
        with self.assertRaises(TypeError) as err:
            self.assertEqual(72, rect.area())
        self.assertEqual("'int' object is not callable", str(err.exception))

    def test_rectangleArea_with_two_args(self):
        self.assertEqual(12, Rectangle(3, 4).area())

    def test_rectangleArea_with_three_args(self):
        self.assertEqual(15, Rectangle(3, 5, 3).area())

    def test_rectangleArea_four_three_args(self):
        self.assertEqual(150, Rectangle(3, 50, 3, 0).area())

    def test_rectangleArea_width_equal_height(self):
        self.assertEqual(100, Rectangle(10, 10, 3, 0).area())

    def test_rectangleArea_after_width_change(self):
        rec1 = Rectangle(10, 10, 3, 0)
        rec1.width = 6
        self.assertEqual(60, rec1.area())

    def test_rectangleArea_after_height_change(self):
        rec1 = Rectangle(3, 1, 3, 0)
        rec1.height = 7
        self.assertEqual(21, rec1.area())

    def test_rectangleArea_after_height_and_width_change(self):
        rec1 = Rectangle(3, 1, 3, 0)
        rec1.height = 7
        rec1.width = 5
        self.assertEqual(35, rec1.area())

    def test_rectangleArea_swap_width_height(self):
        rec1 = Rectangle(8, 7, 3, 0)
        self.assertEqual(56, rec1.area())
        width = rec1.width
        rec1.width = rec1.height
        rec1.height = width
        self.assertEqual(56, rec1.area())

    def test_rectangleArea_change_x(self):
        rec1 = Rectangle(3, 1, 3, 0)
        self.assertEqual(3, rec1.area())
        rec1.x = 1
        self.assertEqual(3, rec1.area())

    def test_rectangleArea_change_y(self):
        rec1 = Rectangle(3, 1, 3, 0)
        self.assertEqual(3, rec1.area())
        rec1.y = 0
        self.assertEqual(3, rec1.area())


class Test_display_stdout(unittest.TestCase):
    """Test if display prints # in stdout"""

    def test_display_attr(self):
        self.assertTrue(hasattr(Rectangle(2, 3), "display"))

    def test_display_args(self):
        rect = Rectangle(9, 8)
        with self.assertRaises(TypeError) as err:
            rect.display("#")
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

    def test_display_with_width_height(self):
        # Create a rectangle and call display
        r1 = Rectangle(4, 6)
        # Use context manager to temporarily redirect stdout
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        # Check if the output is correct
        self.assertEqual(output, "####\n####\n####\n####\n####\n####\n")

    def test_display_swap_width_height(self):
        # Create a rectangle and call display
        r1 = Rectangle(4, 6)
        # Use context manager to temporarily redirect stdout
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        # Check if the output is correct
        self.assertEqual(output, "####\n####\n####\n####\n####\n####\n")

        width = r1.width
        r1.width = r1.height
        r1.height = width
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "######\n" * 4)

    def test_display_with_width_equal_height(self):
        # Create a rectangle and call display
        r1 = Rectangle(4, 4)
        # Use context manager to temporarily redirect stdout
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        # Check if the output is correct
        self.assertEqual(output, "####\n####\n####\n####\n")

    def test_display_with_x_y_zero(self):
        r1 = Rectangle(4, 4, 0, 0)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "####\n####\n####\n####\n")

    def test_display_with_x(self):
        r1 = Rectangle(4, 5, 3)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "   ####\n" * 5)

    def test_display_with_y(self):
        r1 = Rectangle(4, 5, y=3)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n\n\n" + "####\n" * 5)

    def test_display_with_x_equal_y(self):
        r1 = Rectangle(6, 1, 8, 8)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n\n\n\n\n\n\n\n" + "        ######\n")

    def test_display_with_x_notequal_y(self):
        r1 = Rectangle(6, 2, 2, 3)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n\n\n" + "  ######\n" * 2)

    def test_display_with_x_y_equal_one(self):
        r1 = Rectangle(1, 1, 1, 1)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        self.assertEqual(output, "\n" + " #\n")


class TestRectangle_ptint_str(unittest.TestCase):
    """test __str__ method"""

    def test_str_width_height(self):
        Base._Base__nb_objects = 0
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(Rectangle(9, 8))
            stdout_output = buf.getvalue()
        expected_output = "[Rectangle] (1) 0/0 - 9/8\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_width_height_directAccess(self):
        Base._Base__nb_objects = 0
        rect = Rectangle(9, 8)
        expected_output = "[Rectangle] (1) 0/0 - 9/8"
        self.assertEqual(expected_output, rect.__str__())
        self.assertEqual(expected_output, str(rect))

    def test_str_width_height_directAccess(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(9, 8)
            rect.__str__(rect)

    def test_str_width_height_id(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(Rectangle(9, 8, 0, 0, 100))
            stdout_output = buf.getvalue()
        expected_output = "[Rectangle] (100) 0/0 - 9/8\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_width_height_id_x_y(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(Rectangle(9, 8, 7, 9, 100))
            stdout_output = buf.getvalue()
        expected_output = "[Rectangle] (100) 7/9 - 9/8\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_width_height_changed(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            rect = Rectangle(9, 8, 7, 9, 100)
            rect.width = 12
            rect.height = 1
            print(rect)
            stdout_output = buf.getvalue()
        expected_output = "[Rectangle] (100) 7/9 - 12/1\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_id_changed(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            rect = Rectangle(9, 8, 7, 9, 100)
            rect.id = 99
            print(rect)
            stdout_output = buf.getvalue()
        expected_output = "[Rectangle] (99) 7/9 - 9/8\n"
        self.assertEqual(expected_output, stdout_output)

    def test_str_x_y_changed(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            rect = Rectangle(1, 2, 7, 9, 0)
            rect.x = 0
            rect.y = 0
            print(rect)
            stdout_output = buf.getvalue()
        expected_output = "[Rectangle] (0) 0/0 - 1/2\n"
        self.assertEqual(expected_output, stdout_output)


class TestRectangle_update(unittest.TestCase):
    """Test the Rectangle update method"""

    def test_update_attr(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertTrue(hasattr(rect1, "update"))

    def test_update_one_arg(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")

        rect1.update(89)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_arg(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")

        rect1.update(89, 2)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_two_valid_arg(self):
        rect1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as err:
            rect1.update(89, 2.2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_update_three_arg(self):
        rect1 = Rectangle(10, 10, 10, 10, 10)

        rect1.update(89, 2, 3)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_three_valid_arg(self):
        rect1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as err:
            rect1.update(89, 2, "3")
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_update_four_arg(self):
        rect1 = Rectangle(10, 10, 10, 10, 10)

        rect1.update(89, 2, 3, 9)
        self.assertEqual(str(rect1), "[Rectangle] (89) 9/10 - 2/3")

    def test_update_four_valid_arg(self):
        rect1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as err:
            rect1.update(89, 2, 3, "9")
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_update_five_arg(self):
        rect1 = Rectangle(10, 10, 10, 10, 10)

        rect1.update(89, 2, 3, 9, 1)
        self.assertEqual(str(rect1), "[Rectangle] (89) 9/1 - 2/3")

    def test_update_four_valid_arg(self):
        rect1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as err:
            rect1.update(89, 2, 3, 9, "1")
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_update_no_args_kwargs(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update()
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_none(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update(None)
        self.assertEqual(str(rect1), "[Rectangle] (2) 10/10 - 10/10")

    def test_skip_kwargd_one_arg(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update(98, width=3)
        self.assertEqual(str(rect1), "[Rectangle] (98) 10/10 - 10/10")

    def test_skip_kwargd_two_arg(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update(98, 4, height=3, x=1)
        self.assertEqual(str(rect1), "[Rectangle] (98) 10/10 - 4/10")

    def test_skip_kwargd_when_args_None(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update(None, height=3, x=1)
        self.assertEqual(str(rect1), "[Rectangle] (2) 10/10 - 10/10")

    def test_kwargd_with_id_None(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")
        rect1.update(id=None)
        self.assertEqual(str(rect1), "[Rectangle] (2) 10/10 - 10/10")

    def test_kwargd_with_id(self):
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.update(id=50)
        self.assertEqual(str(rect1), "[Rectangle] (50) 10/10 - 10/10")

    def test_kwargd_ordered_width_height(self):
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.id = 1
        rect1.update(width=2, height=3)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 2/3")

    def test_kwargd_height_width(self):
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.id = 1
        rect1.update(height=3, width=2)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 2/3")

    def test_kwargd_ordered(self):
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.update(id=50, width=2, height=3, x=1, y=1)
        self.assertEqual(str(rect1), "[Rectangle] (50) 1/1 - 2/3")

    def test_kwargd_inreverse(self):
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.update(y=1, x=1, height=3, width=2, id=50)
        self.assertEqual(str(rect1), "[Rectangle] (50) 1/1 - 2/3")

    def test_kwargd_three_orderedkeys(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10)
        rect1.update(id=None, width=2, height=3)
        self.assertEqual(str(rect1), "[Rectangle] (2) 0/0 - 2/3")

    def test_kwargd_three_unorderedkeys(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10)
        rect1.update(id=None, y=2, height=3)
        self.assertEqual(str(rect1), "[Rectangle] (2) 0/2 - 10/3")

    def test_kwargd_three_orderedkeys(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.update(id=98, width=2, height=3, x=10)
        self.assertEqual(str(rect1), "[Rectangle] (98) 10/10 - 2/3")

    def test_kwargd_four_unorderedkeys(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10)
        rect1.update(height=3, id=7, x=6, width=6, y=0)
        self.assertEqual(str(rect1), "[Rectangle] (7) 6/0 - 6/3")

    def test_kwargd_not_changing_values(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10, 10)
        rect1.update(height=10, id=10, x=10, width=10, y=10)
        self.assertEqual(str(rect1), "[Rectangle] (10) 10/10 - 10/10")

    def test_kwargd_key_not_exsit(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10, 10)
        rect1.update(h=10)
        self.assertEqual(str(rect1), "[Rectangle] (10) 10/10 - 10/10")


class TestRectangle_to_dictionary(unittest.TestCase):
    """Test to_dictionary method"""

    def test_to_dictionary_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).to_dictionary("dict")

    def test_toDictionary_output(self):
        Base._Base__nb_objects = 0
        r = Rectangle(9, 8)
        excepted_output = {"id": 1, "width": 9, "height": 8, "x": 0, "y": 0}
        # self.assertEqual(r.to_dictionary(), excepted_output)
        self.assertDictEqual(r.to_dictionary(), excepted_output)

    def test_toDictionary_output_after_set_attributes(self):
        Base._Base__nb_objects = 0
        r = Rectangle(9, 8)
        r.id = 10
        r.x = 1
        r.y = 9
        excepted_output = {"id": 10, "width": 9, "height": 8, "x": 1, "y": 9}
        # self.assertEqual(r.to_dictionary(), excepted_output)
        self.assertDictEqual(r.to_dictionary(), excepted_output)

    def test_update_object_with_toDictionary(self):
        Base._Base__nb_objects = 0
        r = Rectangle(9, 8)
        r2 = Rectangle(2, 3)
        self.assertNotEqual(r, r2.update(**r.to_dictionary()))


if __name__ == "__main__":
    unittest.main()
