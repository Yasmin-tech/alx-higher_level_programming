#!/usr/bin/python3
""" This moudle contain one method find_peak
    that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    peak = None

    if (list_of_integers):
        peak = list_of_integers[0]
        flag = False
        for i in range(len(list_of_integers) - 1):
            if list_of_integers[i + 1] > peak:
                peak = list_of_integers[i + 1]
                flag = False
            elif peak == list_of_integers[i + 1]:
                flag = True

    return peak
