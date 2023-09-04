#!/usr/bin/python3
"""Defining a Rectangle class"""


class Rectangle:
    """"
    Instantiation with optional attributes:
        width(int)
        height (int)
    """
    def __init__(self, width=0, height=0):
        """
        Creating new instances of the class Rectangle:
            width (int): set to 0
            height (int): set to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        the width retriever
        returns: width (int) of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        the height retriever
        returns: height (int) of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
