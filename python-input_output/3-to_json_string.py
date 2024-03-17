#!/usr/bin/python3
"""
Converts a string object to JSON
"""


import json

def to_json_string(my_obj):
    """
    Args:
        string (str): The string object to convert

    Returns:
        str: JSON representation.
    """
    return json.dumps(my_obj)
