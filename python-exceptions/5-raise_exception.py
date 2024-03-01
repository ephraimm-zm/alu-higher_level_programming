#!/usr/bin/python3
def raise_exception():
    try:
        raise Exception
    except TypeError as e:
        print(e)
