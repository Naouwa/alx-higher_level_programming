#!/usr/bin/python3
"""Dening a student class based on '9-student.py'"""


class Student:
    """A Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initializing a student
        Agrs:
            first_name: (str)
            last_name: (str)
            age: (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """the dictionary representation of the student"""

        elements = {}

        if attrs is None:
            return (self.__dict__)

        for k in attrs:
            """transforming all keys into dictionary"""
            element = self.__dict__.get(k)
            if element is not None:
                elements[k] = element

        return (elements)
