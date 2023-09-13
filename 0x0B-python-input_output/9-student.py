#!/usr/bin/python3
"""Defining a Class Student"""


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

    def to_json(self):
        """the dictionary representation of the student"""
        return (self.__dict__)
