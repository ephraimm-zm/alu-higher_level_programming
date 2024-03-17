#!/usr/bin/python3
"""
Module for task 101
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible

    Args:
        obj: The object to which the attribute will be added
        attr_name (str): The name of the new attribute
        attr_value: The value of the new attribiute.

    Raise:
        TypeError: If object cannot have a new attribute
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
