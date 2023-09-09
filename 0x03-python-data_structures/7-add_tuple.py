#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ a function that adds 2 tuples.

    The first element should be the addition of the first
    element of each argument

    The second element should be the addition of the
    second element of each argument
    """
    sum_1 = 0
    sum_2 = 0
    a_len = len(tuple_a)
    b_len = len(tuple_b)

# a(1, 2) b(2, 3)
# a(1, ) b(2, 3)
    if a_len >= 2:
        sum_1 += tuple_a[0]  # 1 +
        sum_2 += tuple_a[1]  # 2 +
    elif a_len == 1:
        sum_1 += tuple_a[0]

    if b_len >= 2:
        sum_1 += tuple_b[0]  # 1 + 2 = 3
        sum_2 += tuple_b[1]  # 2 + 3 = 5
    elif b_len == 1:
        sum_1 += tuple_b[0]

    new_tuple = (sum_1, sum_2)
    return new_tuple
