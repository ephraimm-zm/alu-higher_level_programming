#!/usr/bin/python3
"""
Module to write or override text to a specified file.
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): The path to the file to be written
        text (str): The text to be writtted to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
