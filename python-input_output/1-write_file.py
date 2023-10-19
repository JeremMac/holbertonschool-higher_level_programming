#!/usr/bin/python3
'''A module that define write_file function'''


def write_file(filename="", text=""):
    '''a function that writes a string to a text file
    and returns the number of characters written

    args:
        filename: the file we work with.
        text: the text we will write in filename.

    returns:
        the number of characters writen.
    '''

    with open(filename, mode="w", encoding="utf-8") as written_file:
        written_file.write(text)

    return len(text)
