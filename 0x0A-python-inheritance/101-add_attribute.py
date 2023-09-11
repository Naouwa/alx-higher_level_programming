#!/usr/bin/python3
"""Defines a function that adds attributes to obj"""


def add_attribute(obj, att, value):
    """
    It adds an attribute to obj
    Args:
        obj: object
        att: attribute
        value: the value of att
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
