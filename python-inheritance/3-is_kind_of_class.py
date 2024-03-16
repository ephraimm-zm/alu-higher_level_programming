#!/usr/bin/python3
"""
Module for fucntion to check if obj isinstance
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        True if object is instance otherwise False
    """
    return isinstance(obj, a_class)
