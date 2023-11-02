#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    length = len(argv)
    suffix = 'argument' if length > 1 else 'arguments'

    if (length - 1 == 0):
        print("0 arguments.")
    else:
        print('{:d} {:s}:'.format(length - 1, suffix))

    for i in range(1, length):
        print('{:d}: {:s}'.format(i, argv[i]))
