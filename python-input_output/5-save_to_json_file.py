#!/usr/bin/python3
"""
Writes an Object to a text file, using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes the specified object into JSON and writes it to a file

    Args:
        my_obj: The Python object to be serialized.
        filename (str): The path to the file where the JSON will be saved
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
