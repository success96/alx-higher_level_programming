#!/usr/bin/python3
""" This scripts contains a class that defines the attributes of Geometric Shapes,
    method that defines the area of a geometric shape
    and Method that receives the value property
"""


class BaseGeometry:
    """This class defines the attributes of Geometric Shapes """

    def area(self):
        """This method defines the area of a geomtric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method recieves the value property

        Árgs:
            name: name of the object
            value: value of the property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
