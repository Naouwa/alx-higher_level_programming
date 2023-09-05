#!/usr/bin/python3
"""A class with no class or object attribute"""


class LockedClass:
    """the class gets unlocked only if the user inputs 'first_name'"""
    __slots__ = ["first_name"]
