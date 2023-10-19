#!/usr/bin/python3
'''A module that define the append_write function'''


def append_write(filename="", text=""):
    '''A function that appends a string
    at the end of a text file (UTF8) and returns
    the number of characters added

    args:
        filename: the file we will append to.
        text: the text to be added to filename.

    returns: nothing.
    '''

    with open(filename, mode="a", encoding="utf-8") as given_file:
        return given_file.write(text)
