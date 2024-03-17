#!/usr/bin/python3
"""
Module for task 10.square.pu
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square

    Attributes:
        __size (int) : The length of one side of the square
    """

    def __init__(self, size):
        """
        Initializes a Square object with a given size

        Args:
            size (int): The given size of the square/
        """
        size.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area
        """
        return self.__size ** 2
