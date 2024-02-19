#!/usr/bin/python3
"""Defines a base class model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.
    Representds the "base" for all other classes in project 0x0C*
    Attributes:
    __nb_objects (int): The number of instantiated Bases.
    """

    __nd_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
        id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
