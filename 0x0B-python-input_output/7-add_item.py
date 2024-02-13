#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save them to a file
"""


from sys import argv
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


filename = "add_item.json"


try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, filename)
