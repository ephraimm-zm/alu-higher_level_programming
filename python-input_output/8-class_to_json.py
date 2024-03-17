#!/usr/bin/python3
"""
Converts an instance of a class to a dictionary suitable for JSON
"""


def class_to_json(obj):
    """
    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary description of the object
    """
    if not hasattr(obj, '__dict__'):
        return obj

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
        elif hasattr(value, '__dict__'):
            result[key] = class_to_json(value)
    return result
