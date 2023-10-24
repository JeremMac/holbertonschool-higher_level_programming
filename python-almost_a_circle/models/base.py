#!/usr/bin/python3
'''A module with my base class'''
import json


class Base:
    '''A bass class that all our future classes will inherit.

    attribute:
        nb_objects: an attribute that cout the number of objects
                    created with our class.

    instance:
        id: the integer value of the id of our objects.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''A method that that returns the JSON
        string representation of a dictionary'''

        if not list_dictionaries or\
                len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''A method that writes the JSON string
        representation of list_objs to a file.'''
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dict_objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(list_dict_objs))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        else:
            return json.loads(json_string)
