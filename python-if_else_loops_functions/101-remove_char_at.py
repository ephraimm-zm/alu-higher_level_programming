#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    count = 0
    for char in str:
        if count != n:
            result += char
        count += 1
    return result
