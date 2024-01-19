#!/usr/bin/python3

# returns a key with the biggest integer value.

def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[max]:
                max = key
        return max
    return None
