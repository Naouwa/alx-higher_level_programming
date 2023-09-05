#!/usr/bin/python3
""" Adding two integers method"""


def add_integer(a, b=98):
    """Adds two integers.
        Args:
            a: first int.
            b: second int, default value is 98.
        Raises:
            TypeError: if a, b are neither int or float.
        returns:
            sum of integers a and b.
        """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
