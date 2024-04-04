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
    try:
        a = int(a)
    except:
        raise TypeError('a must be an integer')

    try:
        b = int(b)
    except:
        raise TypeError('b must be an integer')

    return a + b
