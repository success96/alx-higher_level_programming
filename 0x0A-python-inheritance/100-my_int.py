#!/usr/bin/python3
""" This script contains a class that inherits from class int
    Method that returns != check
    Method that returns == check
"""


class MyInt(int):
    """ This class inherits from class int"""

    def __eq__(self, other):
        """This method returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """This method returns == check """
        return int.__eq__(self, other)
