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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Serialize a list of object into a JSON file
        Args:
            list_objs (list): A list of instances from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionaries = [
                        obj.to_dictionary()
                        for obj in list_objs
                ]
                file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string into a list of dictionaries
        Args:
            json_string (str): A JSON string
        Returns:
            list: A list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the clas with attributes
        specified in the dictionary.
        Args:
            dictionary (dict): A dictionary containing attributes
            for the instance.
        Returns:
            Base: An instance of the class.
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.
        Returns:
            list: A list of instances loaded from the JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                instances = [
                        cls.create(**data)
                        for data in dictionaries
                        ]
                return instances
        except FileNotFoundError:
            return []
