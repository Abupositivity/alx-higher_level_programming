#!/usr/bin/python3
"""
Contains a write_file function
"""

def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
