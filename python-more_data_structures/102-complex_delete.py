#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []

    for key, current_value in a_dictionary.items():
        if current_value == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]
