#!/usr/bin/python3
"""Json representation module"""
import json


def to_json_string(my_obj):
    """It returns the JSON representation of an object (str)"""
    return json.dumps(my_obj)
