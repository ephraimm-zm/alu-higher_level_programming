#!/usr/bin/python3
"""
Create an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename (str): The path to the JSON file

    Returns:
        obj: The python object deserialized from the JSON file
    """
    with open(filename, 'r') as file:
        return json.load(file)
