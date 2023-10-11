#!/usr/bin/python3
"""This script returns the list of available attribtes
    and methds of an obj
"""


def lookup(obj):
    """This function returns the list of available attribtes
        and methds of an obj

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
