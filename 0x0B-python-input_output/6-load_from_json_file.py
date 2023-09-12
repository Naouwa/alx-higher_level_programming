#!/usr/bin/python3
"""Creacting an object module"""
import json


def load_from_json_file(filename):
    """It creates an object from a 'JSON file'"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        return json.loads(f.read())
