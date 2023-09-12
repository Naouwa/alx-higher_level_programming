#!/usr/bin/python3
"""Dictionary description module"""


def class_to_json(obj):
    """It returns the dictionary with simple data structure,
    for JSON serialization of an object
    """
    return obj.__dict__
