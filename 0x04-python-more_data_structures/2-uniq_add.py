#!/usr/bin/python3

# adds all unique integers in a list.

def uniq_add(my_list=[]):
    add = 0
    for i in set(my_list):
        add += i
    return add
