#!/usr/bin/python3
"""
contains save_to_json_file function
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON repr"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
