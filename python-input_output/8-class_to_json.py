#!/usr/bin/python3
'''A module that defines class_to_json function'''


def class_to_json(obj):
    '''
    A function that returns the dictionary
    description with simple data structure
    for JSON serialization of an object.

    args:
        obj: the object we want the description of.

    returns: the description of obj.
    '''
    return obj.__dict__
