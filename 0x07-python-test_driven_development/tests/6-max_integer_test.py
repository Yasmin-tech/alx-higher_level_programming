#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ A class that contains the test cases for max_integer([..])


    """

    def test_output_of_list(self):
        """ Check the output from a list of integers(positive and negative)
        """
        l_list = [2, -5, 3]
        self.assertEqual(max_integer(l_list), 3)

    def test_list_of_float_and_ints(self):
        """ Check the output from a list of floats and ints
        """
        l_list = [100.1, 2, 3.3, -5, 100]
        self.assertEqual(max_integer(l_list), 100.1)

    def test_list_of_float_and_ints_ordered(self):
        """ Check the output from a list of floats and ints in order
        """
        l_list = [1, 1.0, 1.1, 1.2]
        self.assertEqual(max_integer(l_list), 1.2)

    def test_output_of_list_no_arg(self):
        """ function return None for list = []
        """
        self.assertEqual(max_integer(), None)
        l_list = []
        self.assertEqual(max_integer(l_list), None)

    def test_output_empty_string(self):
        """ function return None for empty string
        """
        string = ""
        self.assertEqual(max_integer(string), None)

    def test_output_of_list_None(self):
        """ The function raises TypeError: object of type 'NoneType'
        has no len() if list is None
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_other_datatype(self):
        """ if all elements same data type then they're comparable
        otherwise: TypeError: '>' not supported between instances of
        'str' and 'int'
        """
        l_list = ["4", "2", "5"]
        self.assertEqual(max_integer(l_list), "5")

        l_list.append(9)
        with self.assertRaises(TypeError):
            max_integer(l_list)

        l_list = (5, 8, 9, 0, -0, 0.0)
        self.assertEqual(max_integer(l_list), 9)

        l_list = (0, -0, 0.0)
        self.assertEqual(max_integer(l_list), 0)

        l_list = (0, -0, 0.0, (0.1, 1))
        with self.assertRaises(TypeError):
            max_integer(l_list)

        l_list = [[9, 9, 11], [10], [11]]
        self.assertEqual(max_integer(l_list), [11])

        l_list = [[12, 9], [10], [11]]
        self.assertEqual(max_integer(l_list), [12, 9])

        l_list = [100, [10], [11]]
        with self.assertRaises(TypeError):
            max_integer(l_list)

        l_list = float('inf')
        "TypeError: object of type 'float' has no len()"
        with self.assertRaises(TypeError):
            max_integer(l_list)

        # one infinite arg
        l_list = [float('inf')]
        self.assertEqual(max_integer(l_list), float('inf'))
