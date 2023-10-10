#!/usr/bin/python3
"""a module with print_square function definition"""


def print_square(size):
    """a function that print a square"""

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print(size * '#')
