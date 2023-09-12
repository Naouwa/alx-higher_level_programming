#!/usr/bin/python3
"""Adding all arguments to a file module"""
import json


def save_to_json_file(my_obj, filename):
    """It adds all arguments to a python list,
    and then save them to a file
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
