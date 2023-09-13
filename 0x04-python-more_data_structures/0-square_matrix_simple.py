#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """  a function that computes the square value of all integers of a matrix

    Arguments: a matrix of integers

    Return: a new matrix of square value of all integers of the input matrix
    """

    new_matrix = []

    for li in matrix:
        sub_li = list(map(lambda x: x ** 2, li))
        new_matrix.append(sub_li)
    return new_matrix
