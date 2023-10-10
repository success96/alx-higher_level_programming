#!/usr/bin/python3
"""
This is a python script which defines a JSON file-reading function.
"""
import json


def load_from_json_file(filename):
    """ This function create a Python object from a JSON file. """
    with open(filename) as f:
        return json.load(f)
