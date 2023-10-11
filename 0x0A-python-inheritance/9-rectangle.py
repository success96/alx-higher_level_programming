#!/usr/bin/python3
"""This script contains a class that defines a rectangle from BaseGeometry Class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a rectangle from BaseGeometry Class"""

    def __init__(self, width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This method returns the area of the instance"""
        return self.__width * self.__height

    def __str__(self):
        """This special method that returns the printable string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
