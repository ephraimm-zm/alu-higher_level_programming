#!/usr/bin/python3
"""
Module to check if an obj is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Args:
    obj: The object to check
    a_class: The class to check against

    Returns:
    True if is instance, False otherwise.
    """
    return isinstance(obj, a_class)
