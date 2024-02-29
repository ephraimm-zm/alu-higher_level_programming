#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lamba x: x**2, row)), matrix))
