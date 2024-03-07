#!/usr/bin/python3
"""
This script defines a Square class representing a square shape.
"""


class Square:
    """
    A class representing a square

    Attributes:
    size (int): The size of the squares sides.
    position (tuple): The position of the squares top left corner.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object with a given size and position

        Params:
        size (int): The size of squares sides
        position (tuple): Postion of squares top left

        Raises:
        TypeError: If size is not an int or position is not a tuple
        ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        int: The size of the squares side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the squares side

        Params:
        value (int): The size to set.

        Raises:
        TypeError: If value is not an int
        ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        tuple: The position of the squares top left corner.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the positoin of the squares top left corner.

        Params:
        value (tuple): The position to set.

        Raises:
        TypeError: If value is not a tuple of two positives ints.
        """
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a graphical representation of the square.
        """
        if self.size == 0:
            print("")
            return
        for _ in range(self.position[1]):
            print()
        for line_num in range(self.size):
            if line_num == self.size - 1:
                print(" " * self.position[0] + "#" * self.size, end="")
            else:
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string rep of the square

        Returns:
        str: The string rep of the square.
        """
        self.my_print()
        return ""
