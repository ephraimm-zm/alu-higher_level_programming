#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_a, second_a = tuple_a[:2] + (0, 0)
    first_b, second_b = tuple_b[:2] + (0, 0)

    first = first_a + first_b
    second = second_a + second_b

    return (first, second)
