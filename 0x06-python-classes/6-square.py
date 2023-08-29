#!/usr/bin/python3
"""no module was imported"""
class Square:
    """defining a class for square generator"""
    def __init__(self, size=0, position=(0, 0)):
        """initialisation of a new square"""
        self.size = size
        self.position = position

    def area(self):
        """it returns the area of a square"""
        return (slef.__size**2)

    @property
    def size(self):
        """getter/setter method"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """
        it prints the square
        """
        if self.__size == 0:
            print()
        else:
            for p in range(self.__position[1]):
                print()
            for a in range(self.__size):
                for s in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(a) is not int for a in value) or any(b < 0 for b in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
