#!/usr/bin/python3
"""
if obj is instance of a class that inherited
frm the specified class.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        True if the object is an instance of a class
        that inherited, otherwise False
    """
    return issubclass(obj.__class__, a_class and obj.__class__ != a_class)
