#!/usr/bin/python3
"""
A script to add arguments to a Python list and save them to a file
"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    # Exclude the script name from arguments
    arguments = sys.argv[1:]

    # Load existing data from file or initialize an empty list
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    # Add arguments to the list
    data.extend(arguments)

    # Save the updated list to file
    save_to_json_file(data, "add_item.json")
