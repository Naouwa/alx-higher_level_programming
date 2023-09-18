#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that's inherited from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intializing class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public methods that assign attributes"""
        if args:
            for argument in range(len(args)):
                if argument == 0:
                    self.id = args[argument]
                if argument == 1:
                    self.size = args[argument]
                if argument == 2:
                    self.x = args[argument]
                if argument == 3:
                    self.y = args[argument]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """Returns a string representation of the Square class"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))
