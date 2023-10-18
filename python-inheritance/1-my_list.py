#!/usr/bin/python3
'''A module that contains MyList class'''


class MyList(list):
    '''a class with that inherits a given list.
    method: print_sorted a function that
    prints a list in sorted order.
    '''
    def print_sorted(self):
        print(sorted(self))
