#!/usr/bin/python3

# computes the square of all integers.

def square_matrix_simple(matrix=[]):
    return[list(map((lambda x: x * x), elm)) for elm in matrix]
