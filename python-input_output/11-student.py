#!/usr/bin/python3
'''A module that contains the Student class.'''


class Student:
    '''A class that creates a student.'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
