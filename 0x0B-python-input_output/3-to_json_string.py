#!/usr/bin/python3
"""
This is a script that defines a string-to-JSON function.
"""
import json


def to_json_string(my_obj):
    """ 
    This function return the JSON representation of a string object.
    """
    return json.dumps(my_obj)
