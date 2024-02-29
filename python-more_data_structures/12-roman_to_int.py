#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
            'I':1, 'V':5, 'X':10, 'L':50, 
            'C':100, 'D':500, 'M':1000
            }
    total = 0
    i = 0
    length = len(roman_string)
    current = roman_dict[roman_string[i]]
    following = roman_dict[roman_string[i+1]]

    while i < length:
        if i + 1 < length and current < following:
            total += following - current
            i += 2
        else:
            total += current
            i += 1

    return total
