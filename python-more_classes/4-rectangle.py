#!/usr/bin/python3
"""a module that contains the my rectangle class"""


class Rectangle:
    """a class that creates a rectangle

    returns a rectangle

    raises:
        TypeError: if width or height are not integers.
        ValueError: if width or height are inferior to zero.
    """

    def __init__(self, width=0, height=0):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        str_rect = ''
        if self.__height != 0 and self.__width != 0:
            for _ in range(self.__height):
                if _ == self.__height - 1:
                    str_rect += '#' * self.__width
                else:
                    str_rect += '#' * self.__width + '\n'
        return str_rect

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
