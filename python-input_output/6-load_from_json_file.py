#!/usr/bin/python3
'''A module that define load_from_json_file'''
import json


def load_from_json_file(filename):
    '''A function that creates an Object from a “JSON file”

    args:
        filename: the json file we will build the object from.

    returns: the created object.
    '''

    with open(filename, encoding="utf-8") as json_obj:
        return json.load(json_obj)
