#!/usr/bin/python3
'''A with a class that raise an error'''


class BaseGeometry:
    '''a class that raise an error message'''

    def area(self):
        raise Exception("area() is not implemented")
