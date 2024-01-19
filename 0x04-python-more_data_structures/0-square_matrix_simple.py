#!/usr/bin/python3

# computes the square values of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    return[list(map((lambda x: x * x), elm)) for elm in matrix]
