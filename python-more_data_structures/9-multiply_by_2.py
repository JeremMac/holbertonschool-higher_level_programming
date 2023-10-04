#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dico = a_dictionary.copy()
    for key, value in new_dico.items():
        new_dico[key] = value * 2
    return new_dico
