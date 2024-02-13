#!/usr/bin/python3
"""
Contains a class Student
"""


class Student:
    """representation of a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dict representation of the Student instance"""
        json_dict = {
            "first_name": self.first_name
            "last_name": self.last_name
            "age": self.age
        }
        return json_dict
