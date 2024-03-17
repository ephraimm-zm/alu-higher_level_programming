#!/usr/bin/python3
import json
"""
Converts a string object to JSON
"""


def to_json_string(my_obj):
    """
    Args:
        string (str): The string object to convert

    Returns:
        str: JSON representation.
    """
    return json.dumps(my_obj)
