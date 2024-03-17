#!/usr/bin/python3
"""define class square"""


class Square:
    """define empty class square"""

    def __init__(self, size=0):
        """define __init__ method"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """define area method"""
        return self.__size ** 2
