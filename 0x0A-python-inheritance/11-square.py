#!/usr/bin/python3
""" This class defines a Sqare from Rectangle class
    Method that initializes a Square
    Method that returns a string with the area
    Special method that returns a printable string
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class defines a Square from Rectangle class """

    def __init__(self, size):
        """This method initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """This method returns a string with the area """
        return super().area()

    def __str__(self):
        """This special method that returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
