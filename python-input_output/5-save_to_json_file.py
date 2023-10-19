#!/usr/bin/python3
'''A module that defines save_to_json_file function.'''
import json


def save_to_json_file(my_obj, filename):
    '''a function that writes an Object
    to a text file, using a JSON representation

    args:
        my_obj: the object we want to work with.
        filename: the file we will write the json representation
                of my_obj in.
    '''

    with open(filename, mode="w", encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
