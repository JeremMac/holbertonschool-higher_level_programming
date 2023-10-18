#!/usr/bin/python3
'''A module that define the lookup function'''


def lookup(obj):
    '''A function that returns a list of instances
    in an object.
    '''
    return dir(obj)
