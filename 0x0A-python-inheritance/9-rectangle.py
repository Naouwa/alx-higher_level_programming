#!/usr/bin/python3
"""Defines a Recrangle class that inherits from BaseGeometry base on task 7"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Initializing a new rectangle
        Args:
            width: int
            height: int
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """It returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """It return the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
