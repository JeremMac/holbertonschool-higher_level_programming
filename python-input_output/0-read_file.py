#!/usr/bin/python3
'''A module that define read_file function'''


def read_file(filename=""):
    '''A function that reads a file and prints it content.

    args:

    filename=""  a variable with the name of the file to be read.

    returns: nothing.
    '''

    with open(filename, encoding="utf-8") as given_file:
        print(given_file.read())
