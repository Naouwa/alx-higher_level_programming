#!/usr/bin/python3
"""Defines a function that checks for same class"""


def is_same_class(obj, a_class):
    """
    it determines if obj is an instance of a_class.
    args:
        obj: object to look for
        a_class: class to verify
    returns:
        True: if the object is exactly an instance of the specified class
        False: if it's not
    """

    if type(obj) is a_class:
        return True
    return False
