#!/usr/bin/python3

#removes all characters c and C from a string.

def no_c(my_string):
    new_s = my_string.translate({ord('c'): None})
    new_s = my_s.translate({ord('C'): None})
    return new_s
