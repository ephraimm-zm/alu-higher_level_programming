#!/usr/bin/python3
"""
Some magic calculation

This module defines a class, MagicClass, which performs some magical calculations.
"""

import math

class MagicClass:
    def __init__(self, radius):
        """
        Initialize MagicClass with a given radius.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int or \
                type(radius) is not float:
                    raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Calculate the circumference of the circle

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

