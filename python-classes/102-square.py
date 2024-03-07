#!/usr/bin/python3
"""
Initialize a Square object with the given size.
"""

class Square:
    def __init__(self, size):
        """
        Args:
            size(int): The size of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """
        int: The size of the squares sides
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the squares sides

        Params:
        value (int): The size to set.

        Raises:
        TypeError: If the value is not an int
        ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if this square is equal to another square based on their areas

        Args:
        other (Square): The other square to compare.

        Returns:
        bool: Based on the areas of both squares
        """
        if isinstance(other, Square):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        """
        Check if this square is not equal to another square based on their areas

        Args:
        other (Square): The other square to compare.

        Returns:
        bool: True if areas of both are not equal, otherwise false
        """
        if isinstance(other, Square):
            return self.area != other.area
        return NotImplemented

    def __gt__(self, other):
        """
        Check if this square is greater than another based on their areas
        Args:
        other (Square): The other square to compare.

        Returns:
        bool: True if area of this square is greater than area of other square
        """
        if isinstance(other, Square):
            return self.area > other.area
        return NotImplemented

    def __ge__(self, other):
        """
        Check if this square is greater than or equal to another

        Args:
        other (Square): The other square

        Returns:
        bool: True is this square is greater than the other
        """
        if isinstance(other, Square):
            return self.area >= other.area
        return NotImplemented

    def __lt__(self, other):
        """
        Check if this square is less than another based on areas

        Args:
        other (Square): The other square

        Returns:
        bool: True if this square is less than the other
        """
        if isinstance(other, Square):
            return self.area < other.area
        return NotImplemented

    def __le__(self, other):
        """
        Check if this square is less than or equal to another based on areas
        Returns: True or false
        """
        if isinstance(other, Square):
            return self.area <= other.area
        return NotImplemented
