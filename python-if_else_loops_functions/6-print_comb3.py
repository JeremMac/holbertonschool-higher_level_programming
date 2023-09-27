#!/usr/bin/python3
for i in range(0, 10):
    for i2 in range(i + 1, 10):
        if not (i == 8 and i2 == 9):
            print("{}{}".format(i, i2), end=", ")
print("89")
