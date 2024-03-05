#!/usr/bin/python3
"""
This script defines a Square class representing a square shape.
"""


class Square:
    """
    Represents a square object.

    Attributes:
    __size (int): The size of the square.

    Methods:
    __init__: Initializes the Square object with a given size.
    area: Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Parameters:
        size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Parameters:
        value (int): The new size of the square.

        Raises:
        TypeError: if the size is not an integer.
        ValueError: if the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2
