#!/usr/bin/python3
'''A module with my base class'''


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
