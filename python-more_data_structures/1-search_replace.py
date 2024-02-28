#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for char in my_list:
        if char == search:
            result.append(replace)
        else:
            result.append(char)
    return result
