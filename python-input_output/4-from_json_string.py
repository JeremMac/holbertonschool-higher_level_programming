#!/usr/bin/python3
'''A module that defines the from_json_string function'''
import json


def from_json_string(my_str):
    '''A function that returns an object
    represented by a JSON string.

    args:
        my_str: the string we need to convert.

    returns: an object from my_str.
    '''

    return json.loads(my_str)
