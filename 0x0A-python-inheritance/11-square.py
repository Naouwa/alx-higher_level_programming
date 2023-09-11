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
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """it calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """representation string of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
