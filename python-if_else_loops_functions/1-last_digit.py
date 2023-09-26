#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    last_digit = (number % -10) * -1
else:
    last_digit = number % 10

if (last_digit > 5):
    greater = 'and is greater than 5'
    print(f"Last digit of {number} is {last_digit} {greater}")
elif(last_digit < 6):
    less = 'and is less than 6 and not 0'
    print(f"Last digit of {number} is {last_digit} {less}")
else:
    zero = 'and is 0'
    print(f"Last digit of {number} is {last_digit} {zero}")
