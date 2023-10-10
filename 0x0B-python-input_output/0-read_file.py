#!/usr/bin/python3

"""
Defines a function that reads text from a file
"""
def read_file(filename=""):
    """
    This function print the contents of a UTF8 text file to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")