#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set()

    for element in set_1:
        if element in set_2:
            common.add(element)
    result = (set_1.union(set_2)).difference(common)

    return result
