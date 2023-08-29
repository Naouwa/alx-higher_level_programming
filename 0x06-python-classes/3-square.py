#!/usr/bin/python3
"""
    no module was imported
 """
class Square:
    """ args - size (int): length of one side
        Attributes - __size (int): length of one side
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ 
        it calculates the area of a Square
        """
        return self.__size**2


