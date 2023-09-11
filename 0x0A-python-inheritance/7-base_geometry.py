#!/usr/bin/python3
"""Defines a BaseGeometry class based on task6"""


class BaseGeometry:
    """an empty class"""

    def area(self):
        """It calculates the area"""

        raise Exception("area() is nit implemented")

    def integer_validator(self, name, value):
        """it validates a number as integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
