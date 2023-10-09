#!/usr/bin/python3
"""a module with my class"""


class Square:
    """a class with the size of a square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """a function that returns the square value of size"""
    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is True:
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        for i in range(self.__size):
            print(self.size * '#')
