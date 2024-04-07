#!/usr/bin/python3
"""
Module for function that prints a square with # char
"""


def print_square(size):
    """
    Args:
        size: The size of the square
    Raises:
        TypeError: If size is not an int
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
