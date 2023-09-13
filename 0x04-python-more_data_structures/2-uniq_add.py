#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ a function that adds all unique integers in a list
      (only once for each integer).

      Argument: the list

      Return: the sum of all the unique elements
      """

    if not my_list:
        return 0
    return sum(set(my_list))
