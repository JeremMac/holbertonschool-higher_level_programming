#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    le = 0
    try:
        for i in my_list:
            if le < x:
                print("{}".format(i), end="")
                le += 1
        print()
        return (le)
    except IndexError:
        print()
