#!/usr/bin/python3
"""
Module for function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function to validate and multiply matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                        "m_a should contain only integers or floats"
                        )
    if len(set(len(row) for row in m_a)) != 1:
        raise ValueError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) != 1:
        raise ValueError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
                row.append(total)
            result_matrix.append(row)

    return result_matrix
