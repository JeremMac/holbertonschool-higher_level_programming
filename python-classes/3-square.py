#!/usr/bin/python3
"""an module with my class"""


class Square:
    """a class with the size of a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """a function that returns the square value of size"""
    def area(self):
        area = self.__size * self.__size
        return area
