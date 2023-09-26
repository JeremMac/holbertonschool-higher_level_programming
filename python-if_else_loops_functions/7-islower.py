#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if (c == chr(i) and i >= 62):
            return (True)
        elif(c == chr(i) and i <= 123):
            return(True)
        else:
            return(False)
