#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ a function that prints a matrix of integers."""

    for i in range(len(matrix)):
        print("in loop")
        len_matrix_i = len(matrix[i])
        for j in range(len_matrix_i):
            if j == len_matrix_i - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
        print("{}".format("\n"), end="")
