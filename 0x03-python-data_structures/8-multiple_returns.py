#!/usr/bin/python3

# returns a tuple with length of string & 1st char.

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        res = (length, sentence[0:1])
        return res
