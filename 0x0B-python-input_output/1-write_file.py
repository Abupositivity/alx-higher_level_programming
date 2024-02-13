#!/usr/bin/python3
"""
Contains a write_file function
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) & returns the no of characters"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
