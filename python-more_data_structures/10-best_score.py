#!/usr/bin/python3
def best_score(a_dictionary):
    highest = 0
    highest_key = None

    if not a_dictionary:
        return None

    for key, value in a_dictionary.items():
        if value > highest:
            highest = value
            highest_key = key

    return highest_key
