#!/usr/bin/python3
"""
Converts JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str (str): The JSON string
    Returns:
        obj: The python object
    """
    return json.loads(my_str)
