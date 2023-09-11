#!/usr/bin/python3
"""Defines a rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a Square class"""

    def __init__(self, size):
        """
        Initilizing a new square
        Args:
            size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
