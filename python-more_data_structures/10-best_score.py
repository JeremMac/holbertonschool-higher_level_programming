#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    high_value = 0
    the_key = None
    for key, value in a_dictionary.items():
        if value > high_value:
            the_key = key
            high_value = value
    return the_key
