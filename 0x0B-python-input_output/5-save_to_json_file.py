#!/usr/bin/python3
"""Writing an object module"""
import json


def save_to_json_file(my_obj, filename):
    """
    It writes an object to a text file,
    using a JSON representation
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
