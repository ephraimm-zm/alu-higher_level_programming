#!/usr/bin/python3
"""
Module for function to print string with 2 new lines after given chars
"""


def text_indentation(text):
    """
    Args:
        text: The input string

    Raises:
        TypeError: If text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += '\n\n'
    print(result.strip())
