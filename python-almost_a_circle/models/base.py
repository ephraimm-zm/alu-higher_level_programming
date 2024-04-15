#!/usr/bin/python3
"""
Module for class that will Base of other classes
"""
import json


class Base:
    """
    Base class for other classes.
    Atribues:
        __nb_objects (int): Number of objects created.
        id (int): Identifier for the object
    """
    __nb_objects = 0

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
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serialize a list of dictionaries into a JSON string
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: A JSON string representaion of list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
