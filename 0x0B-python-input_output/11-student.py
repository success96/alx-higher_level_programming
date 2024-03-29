#!/usr/bin/python3
"""
This file defines a class Student.
"""


class Student:
    """
    This class represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        This helps initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        This replaces all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for i, j in json.items():
            setattr(self, i, j)
