#!/usr/bin/python3
"""
contains class_to_json function
"""


def class_to_json(obj):
    """ returns the dict description with simple data struct for json"""
    json_dict = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
