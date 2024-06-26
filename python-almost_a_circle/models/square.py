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

    def update(self, *args, **kwargs):
        """
        Updates the square attributes based on arguments given

        Args:
            *args (list): List of arguments
            **kwargs (dict): Dictionary of keyword arguments
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns string representaion of the square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
