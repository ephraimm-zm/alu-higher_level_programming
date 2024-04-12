#!/usr/bin/python3
"""
Module for Rectangle class that inherits from Base
"""


from models import base

class Rectangle(Base):
    """
    A class representing a rectangle

    Inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int, optional): The x-cordinate of top left corner
            y (int, optional): The y-cordinate top right corner
            id (int, optional): The ID of rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: The width of the rectangle"""
        return self.width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The new width value
        """
        self.width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value
        """
        self.height = value

    @property
    def x(self):
        """int: the x cordinate for top left of rectangle"""
        return self.x

    @x.setter
    def x(self, value):
        """
        Sets the x cordinate of top left of rectangle
        
        Args:
            value(int): The new x-cordinate value
        """
        self.x = value

    @property
    def y(self):
        """The y cordinate of top left rectangle"""
        return self.y

    @y.setter
    def y(self, value):
        """
        Sets the y-cordinate of the top left rectangle

        Args:
            value (int): The new y cordinate value
        """
        self.y = value
