#!/usr/bin/python3
'''A module that contains a square class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    '''a class that creates a square'''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
