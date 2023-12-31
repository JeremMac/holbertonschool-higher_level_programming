#!/usr/bin/python3
"""a module that defines add_integer function"""


def add_integer(a, b=98):
    """a function that adds two integers

    returns the sum of two integers

    raises:
        TypeError: if a or b are not integers
    """

    if isinstance(a, float) is True:
        a = int(a)
    if isinstance(b, float) is True:
        b = int(b)
    if isinstance(a, int) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False:
        raise TypeError("b must be an integer")
    return a + b
