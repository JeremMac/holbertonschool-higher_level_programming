#!/usr/bin/python3
'''A module with my base class'''
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
