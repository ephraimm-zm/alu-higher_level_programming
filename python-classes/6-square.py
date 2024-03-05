#!/usr/bin/python3
"""
This script defines a Square class representing a square shape.
"""


class Square:
    """
    Represents a square object.

    Attributes:
    __size (int): The size of the square.
    __position (tuple): The position of the square.

    Methods:
    __init__: Initializes a Square object with a given size and position.
    size: Getter method for retrieving the size of the square.
    size: Setter method for setting the size of the square.
    position: Getter method for retrieving the position of the square.
    position: Setter method for setting the position of the square.
    area: Calculates the area of the square.
    my_print: Prints the square using the '#' character, considering the position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a given size and position.

        Parameters:
        size (int): The size of the square.
        position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

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
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Parameters:
        value (tuple): The new position of the square.

        Raises:
        TypeError: If the position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or value[0] < 0 or value[1] < 0:
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
        Prints the square using the '#' character, considering the position.
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
