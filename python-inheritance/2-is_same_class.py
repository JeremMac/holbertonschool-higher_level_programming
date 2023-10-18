#!/usr/bin/python3
'''A module that define is_same_class function.'''


def is_same_class(obj, a_class):
    '''a function that returns true if an instance is from a class.'''

    return type(obj) == a_class
