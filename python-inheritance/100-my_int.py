#!/usr/bin/python3
"""
Module for task 100
"""


class MyInt(int):
    """
    A class that inherits from another but overrides things
    """

    def __eq__(self, other):
        """
        Inverts the behaviour of == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behaviour of != operator.
        """
        return super().__eq__(other)
