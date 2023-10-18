#!/usr/bin/python3
'''A module that define inherits_from function'''


def inherits_from(obj, a_class):
    '''A function that that indicates if the object is an instance
    of a class that inherited from the specified class

    obj: a obj we will work with.
    a_class: the class obj will inherits from or not.

    return: true if obj inherited from a_class
    otherwise return false.
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
