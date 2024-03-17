#!/usr/bin/python3
"""
Appends a string at the end of a text file.
"""


def append_file(filename="", text=""):
    """
    Args:
        filename (str): The path to the file
        text (str): The text to be appended
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
