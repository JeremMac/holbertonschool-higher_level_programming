#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    result = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(roman_string)):
        current = rom[roman_string[i]]
        if i < len(roman_string) - 1 and current < rom[roman_string[i + 1]]:
            result -= rom[roman_string[i]]
        else:
            result += rom[roman_string[i]]
    return result
