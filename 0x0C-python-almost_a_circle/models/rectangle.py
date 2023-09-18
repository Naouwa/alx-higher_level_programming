#!/usr/bin/python3
"""Defines a Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """creating a Rectangle class inherited from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """It calculates the area of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """It prints the Rectangle using the character '#'"""
        rect = self.y * "\n"
        for _ in range(self.height):
            rect += (" " * self.x)
            rect += ("#" * self.width) + "\n"

        print(rect, end="")

    def __str__(self):
        """It returns the string representation of the Rectangle class"""
        str_rect = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.__x, self.__y)
        str_widHei = "{}/{}".format(self.__width, self.__height)

        return str_rect + str_id + str_xy + str_widHei

    def update(self, *args, **kwargs):
        """Assigning arguments to each attribute"""
        if args is not None and len(args) != 0:
            list_attributes = ["id", "width", "height", "x", "y"]
            for argIndex, argValue in enumerate(args):
                if argIndex < len(list_attributes):
                    setattr(self, list_attributes[argIndex], argValue)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
