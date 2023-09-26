#!/usr/bin/python3
for i in range(97, 123):
    alpha = chr(i)
    if (alpha == 'e' or alpha == 'q'):
        alpha = ""
    print("{}".format(alpha), end="")
