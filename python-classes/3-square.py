#!/usr/bin/python3
"""
This script defines a Square class representing a square shape.
"""


class Square:
    """"
    Represents a square object.

    Attributes:
    __size (int): The size of the square.

    Methods:
    __init__: Initializes a Square object with a given size.
    area: Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Parameters:
        size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2
