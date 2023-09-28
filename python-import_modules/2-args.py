#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as arg
i = 1
length = (len(arg)) - 1
if (length < 1):
    print("{} arguments.".format(length))
elif (length == 1):
    print("{} argument:".format(length))
    print("{}: {}".format(length, arg[1]))
else:
    print("{} arguments:".format(length))
    while (i <= length):
        print("{}: {}".format(i, arg[i]))
        i += 1
