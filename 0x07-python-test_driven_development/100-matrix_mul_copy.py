#!/usr/bin/python3
""" This Module contains one function that multiplies 2 matrices



"""


def matrix_mul(m_a, m_b):
    """
        this function takes two matrix of int or floats and 
        multiplies each element in each column of matrix 1
        by each element in each row in matrix 2 
    """
    # m_a or m_b is not a lis
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # m_a or m_b is not a list of lists
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    # m_a or m_b is empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # if one element of those list of lists is not an integer or a float
    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for i in range(len(m_b)):
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    # m_a or m_b is not a rectangle
    a_element = len(m_a[0])
    for row in m_a:
        if len(row) != a_element:
            raise TypeError("each row of m_a must be of the same size")

    b_element = len(m_b[0])
    for row in m_b:
        if len(row) != b_element:
            raise TypeError("each row of m_a must be of the same size")

    # f m_a and m_b can’t be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    b_c = -1
    res = [[0 for _ in range(len(m_a))] for _ in range(len(m_b[0]))]
    for a_r in range(len(m_a)):
        b_c += 1
        b_list = [m_b[r][b_c] for r in range(len(m_b))]
        print("b_list", b_list)
        new_element = 0
        element_in_col_b = 0
        for a_c in range(len(m_a[a_r])):
            new_element = new_element + \
                (m_a[a_r][a_c] * b_list[element_in_col_b])
            element_in_col_b += 1
        print(new_element)
        res[a_r][b_c] = new_element

    return (res)
