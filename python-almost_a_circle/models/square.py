#!/usr/bin/python3
"""
Module for a Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square

    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square
            x (int, optional): The x cordinate of top left corner
            y (int, optional): The y cordinate of top left corner
            id (int, optional): The ID of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """int: The size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): The new size value
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Override __str__ method to provide string representation
        of square
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
                )
