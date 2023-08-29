#!/usr/bin/python3
"""no module was imported"""
class Square:
    """class defined for square generation"""
    def __init__(self, size=0):
        """initialising the square"""
        self.size = size

    def area(self):
        """it returns the area of a square"""
        return self.__size**2

    @property
    def size(self):
        """getter/setter with same method name,
        it returns the length of __size(int)"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """it prints the square with hash character"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()
