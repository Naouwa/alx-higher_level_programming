#!/usr/bin/python3
"""Defines a class MyInt that inherits from integer"""


class MyInt(int):
    """It inverts integer operators != and =="""

    def __eq__(self, value):
        """it iverts == """
        return self.real is not value

    def __ne__(self, value):
        return self.real is value
