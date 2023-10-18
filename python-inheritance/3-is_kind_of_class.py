#!/usr/bin/python3
'''A module that define is_kind_of_class function'''


def is_kind_of_class(obj, a_class):
    '''a function to determine if obj is part of a class

    obj: an instance passed to our function.
    a_class: the class obj is supposed to be a part of.

    return: true if obj is part of a_class
    otherwise return false.
    '''
    return isinstance(obj, a_class)
