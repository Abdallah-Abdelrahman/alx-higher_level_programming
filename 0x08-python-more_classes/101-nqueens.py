#!/usr/bin/python3

"""This module solves the N queens problem.

The N queens puzzle is the challenge of placing N non-attacking queens,
on an N×N chessboard.

Attributes:
    _len: length of the arguments to program.
    num: integer value of 1st arg.
"""

from sys import argv


_len = len(argv)

if _len != 2:
    print('Usage: nqueens N')
    exit(1)

for i in argv[1]:
    if ord(i) < 48 or ord(i) > 57:
        print('N must be a number')
        exit(1)

num = int(argv[1])

if int(num) < 4:
    print('N must be at least 4')
    exit(1)


def queens(n, i, a, b, c):
    """solve N queen using backtrack algorithm

    Using generator function
    """

    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


for solution in queens(num, 0, [], [], []):
    print([[row, col] for row, col in enumerate(solution)])
