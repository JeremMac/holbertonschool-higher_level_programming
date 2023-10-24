#!/usr/bin/python3
'''A module that contains the Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A class that creates a square.

    instances:
        size: the int value of the width and height of Square.
        x: axe position for Square.
        y: second axe Position for square.
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
