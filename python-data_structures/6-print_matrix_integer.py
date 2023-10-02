#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)
    for i in matrix:
        for num in i:
            print("{:d}".format(num), end="")
            if num != (len(matrix)):
                print(" ", end="")
        print()
