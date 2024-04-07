#!/usr/bin/python3
"""
Module for function to print string with 2 new lines after given chars
"""


def text_indentation(text):
    """
    Args:
        text: The input string
    Raises
        TypeError: If text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += '\n\n'
            skip_space = True

        elif char.isspace() and skip_space:
            continue
        else:
            skip_space = False

    print(result.strip(), end="")
