#!/usr/bin/python3
""" This module contains one function `matrix_divided(matrix, div)`

The function takes a list of list of int/float and devide each element by div
"""


def matrix_divided(matrix, div):
    """ thisfunction returns a new matrix after dividing each element by div
    """
    size_of_raw = 0
    if matrix is not None and matrix:
        size_of_raw = len(matrix[0])
        new_matrix = [[element for element in raw] for raw in matrix]
    else:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for raw in range(len(matrix)):
        if type(matrix[raw]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if len(matrix[raw]) != size_of_raw:
            raise TypeError("Each row of the matrix must have the same size")

        for column in range(len(matrix[raw])):

            if type(matrix[raw][column]) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
            if type(div) not in [int, float]:
                raise TypeError("div must be a number")

            if div == 0:
                raise ZeroDivisionError("division by zero")

            new_element = round((matrix[raw][column] / div), 2)
            new_matrix[raw][column] = new_element

    return new_matrix
