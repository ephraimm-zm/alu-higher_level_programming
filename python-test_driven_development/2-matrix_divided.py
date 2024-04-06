#!/usr/bin/python3
"""
Module for function to divide all elements of matrix by divisor
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of lists
        div: The divisor

    Returns:
        list of lists: With elements divided by divisor, rounded to 2

    Raises:
        TypeError
        ZeroDivisionError
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    result = [[round(item / div, 2) for item in row] for row in matrix]

    return result
