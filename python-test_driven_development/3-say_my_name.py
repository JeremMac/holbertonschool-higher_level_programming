#!/usr/bin/python3
"""a module that contains say_my_name function definition"""


def say_my_name(first_name, last_name=""):
    """a function to print last name and first name"""

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
