#!/usr/bin/python3
for i in range(0, 99):
    print("{}, ".format(str(i).zfill(2)), end="")
    if (i == 98):
        print("99")
