#!/usr/bin/python3
"""
no module was imported
"""
class Square:
    """
    class define for square generator
    """
    def __init__(self, size=0):
        """initialize the square"""
        self.size = size

    def area(self):
         """it returns the area of the square"""
         return (self.__size**2)

    @property
    def size(self):
        """ __size getter,setter withe same method name
        it returns __size (int): length
        """
        return self.__size

    @size.setter
    def size(self, value):
        """the property setter for size """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")




