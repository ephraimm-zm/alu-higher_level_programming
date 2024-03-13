#!/usr/bin/python3
"""
This module defines a LockedClass.
"""
class LockedClass:
    """
    Class to only permit instance attrributes named first_name
    
    Attributes:
    __slots__: A list containing the allowed attribute names.
    """
    __slots__ = ['first_name']
