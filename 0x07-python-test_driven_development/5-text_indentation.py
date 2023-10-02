#!/usr/bin/python3
""" This module contains only one function `text_indentation(text)'

The function takes a string as an input and print 2 extera new lines
if the line ends with ., : or ?
"""


def text_indentation(text):
    """ a function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for ch in text:
        if ch == " " and flag:
            continue
        print(ch, end="")
        flag = 0

        if ch == "?" or ch == ":" or ch == ".":
            print("\n")
            flag = 1
