#!/usr/bin/python3
"""This script contains a class that defines a Square from Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This Class defines a Square from Rectangle class """

    def __init__(self, size):
        """Yhis method initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """This method returns a string with the area """
        return super().area()
