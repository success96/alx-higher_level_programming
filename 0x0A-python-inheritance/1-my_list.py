#!/usr/bin/python3
""" This scripts contains a Class that inherits the attributes references of class list
"""


class MyList(list):
    """This Class inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ This method prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
