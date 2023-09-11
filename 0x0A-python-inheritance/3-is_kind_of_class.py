#!/usr/bin/python3
"""Defines a class and inherited class checking functiom"""


def is_kind_of_class(obj, a_class):
    """
    It checks if an object is an instance or inherited of a class
    Args:
        obj: object to check
        a_class: the class to check
    Returns:
        True: if obj is an instance or inherited
        False: otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
