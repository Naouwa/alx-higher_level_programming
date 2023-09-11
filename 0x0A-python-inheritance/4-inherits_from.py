#!/usr/bin/python3
"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """
    It check if an obj is inherited
    Args:
        obj: the object to check
        a_class: the class to check
    Returns:
        True: of object is inherited
        False: otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
