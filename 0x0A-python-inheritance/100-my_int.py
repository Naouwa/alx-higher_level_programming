#!/usr/bin/python3
"""Defines a class MyInt that inherits from integer"""


class MyInt(int):
    """It inverts integer operators != and =="""

    def __eq__(self, value):
        """it iverts == operator"""
        if self is not other_int:
            return False
        return True

    def __ne__(self, value):
        if self is other_int:
            return False
        return True
