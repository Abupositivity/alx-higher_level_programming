#!/usr/bin/python3
"""
Contains the clas "Student"
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of the Student instance.
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        Args:
        attrs(list): (Optional) The attributes  to represent """
    if (type(attrs) == list and
            all(type(ele) == str for ele in attrs)):
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
    return self.__dict__
