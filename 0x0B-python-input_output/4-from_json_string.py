#!/usr/bin/python3
"""Retuening an object module"""
import json


def from_json_string(my_str):
    """It returns an object represented by JSON str"""
    return json.loads(my_str)
