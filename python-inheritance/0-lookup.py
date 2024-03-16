#!/usr/bin/python3
"""
A function to lookup attributes and methods of an object.
"""


def lookup(obj):
    """
    Args:
    obj: The object to inspect

    Returns:
    A list of strings containing the names of available attributes
    and methods of the object
    """
    return dir(obj)
