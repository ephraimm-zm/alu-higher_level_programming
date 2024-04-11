#!/usr/bin/python3
"""
Module for class that will Base of other classes
"""


class Base:
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
