#!/usr/bin/python3
""" In this module, we have a function that opens and read a file
"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="UTF8") as f:
        file_content = f.read()
        print(file_content, end="")
