#!/usr/bin/python3
"""
Module for task 100
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a string after a specific string in a file

    Args:
        filename (str): The name of the file to be modified
        search_string (str): The string to search for in the file
        new_string (str): The string to append after the search_string
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
