#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (not matrix or (len(matrix) == 1 and not matrix[0])):
        print()
        return
    for row in matrix:
        for col in row:
            print('{:d}'.format(col), end=' ' if col != row[-1] else None)
