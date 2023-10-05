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

    new_line = 0
    lines = text.split("\n")
    for line in lines:
        trimmed_line = line.strip()

        for ch in trimmed_line:
            if ch == " " and new_line:
                continue
            print(ch, end="")
            new_line = 0

            if ch == "?" or ch == ":" or ch == ".":
                print("\n")
                new_line = 1
