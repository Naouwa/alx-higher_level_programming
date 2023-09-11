#!/usr/bin/python3
"""Defines a class MyInt that inherits from integer"""


class MyInt(int):
    """It inverts integer operators != and =="""

    def __eq__(self, value):
        """it iverts == operator"""
        return self.real is not value

    def __ne__(self, value):
        """it inverts != operator"""
        return self.real is value
