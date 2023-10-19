#!/usr/bin/python3
'''A module that contains to_json_string function.'''
import json


def to_json_string(my_obj):
    '''a function that returns the JSON
    representation of an object

    args:
        my_obj: the object the function will work with.

    returns: the json representation of my_obj.
    '''
    return json.dumps(my_obj)
