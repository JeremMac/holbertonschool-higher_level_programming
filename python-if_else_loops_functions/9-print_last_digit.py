#!/usr/bin/python3
def print_last_digit(number):
    num = 0
    if (number < 0):
        num = (number % -10) * -1
    else:
        num = number % 10

    print(num, end="")
    return (num)
