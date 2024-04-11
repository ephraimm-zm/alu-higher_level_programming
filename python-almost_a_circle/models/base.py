#!/usr/bin/python3
"""
Module for class that will Base of other classes
"""


class Base:
    """
    Base class for other classes.
    
    Atribues:
        __nb_objects (int): Number of objects created.
        id (int): Identifier for the object
    """
    __nb_object = 0

    def __init__(self, id=None):
        """
        Initializes a base object

        Args:
            id (int): Identifier for object
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
