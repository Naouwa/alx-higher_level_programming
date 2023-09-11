#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):
    """Class with method print_sorted"""

    def print_sorted(self):
        """it prints a list in sorted ascending order"""
        print(sorted(self))
