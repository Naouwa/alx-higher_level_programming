#!/usr/bin/python3
"""
no module was imported
"""
class Square:
    """
    the defined class for square generator
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
