#!/usr/bin/python3
"""
Module for Rectangle class that inherits from Base
"""


from models.base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: the x cordinate for top left of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x cordinate of top left of rectangle
        Args:
            value(int): The new x-cordinate value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y cordinate of top left rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-cordinate of the top left rectangle

        Args:
            value (int): The new y cordinate value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate are of rectangle"""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Override __str__ method to provide string representation of rec
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )

    def update(self, *args, **kwargs):
        """
        Update the rectangle attributes from given args
        *args: Variable number of arguments.
        """
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
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
