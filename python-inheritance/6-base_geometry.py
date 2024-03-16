#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    class called BaseGeometry that raises
    not implemented exception
    """
    def area(self):
        raise Exception("area() is not implemented")
