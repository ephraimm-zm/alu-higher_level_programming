#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result += a  # LOAD_FAST a
    result **= b # BINARY_POWER
    result += a  # BINARY_ADD
    return result
