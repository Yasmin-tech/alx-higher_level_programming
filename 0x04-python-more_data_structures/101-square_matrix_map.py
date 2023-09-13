#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sub_l: list(map(lambda x: x ** 2, sub_l)), matrix))
