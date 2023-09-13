#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x ** 2, sub_list)) for sub_list in matrix]
