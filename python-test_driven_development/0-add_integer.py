#!/usr/bin/python3
"""
This module provides funtion for adding two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Returns:
    int: Su of two ints

    Raises:
    TypeError: If either a or b cannot be cast to an int
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
