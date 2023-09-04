#!/usr/bin/python3
""" Defining a Rectangle class """


class Rectangle:
    """ Instantiation with optional attributes:
        width(int)
        height (int)
    """
    number_of_instances = 0
    print_symbol = "#"
    # public class attributes

    def __init__(self, width=0, height=0):
        """
        Creating new instances of the class Rectangle:
            width (int): set to 0
            height (int): set to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        the width retriever
        returns: width (int) of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        the height retriever
        returns: height (int) of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ The Rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ The Rectangle perimeter:
            returns (width + height) * 2
            or 0 if ( height or width = 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints a rectangle with giving a character"""
        if self.__width == 0 or self.height == 0:
            return ("")
        s = (((str(self.print_symbol) * self.width) + "\n") * self.height)[:-1]
        return s

    def __repr__(self):
        """
        returns a string representation &
        recreates a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """It prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        a method that return the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
