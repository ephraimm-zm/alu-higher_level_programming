#!/usr/bin/python3
"""
Module for task 9
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns:
            dict: Dictionary representation of Student instance

        Args:
            attrs (list): Optional list of attribute names
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
