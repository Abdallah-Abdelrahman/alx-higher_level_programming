#!/usr/bin/python3

from sys import argv

if (__name__ == '__main__'):
    add_up = 0
    length = len(argv)

    for i in range(1, length):
        add_up += int(argv[i])
    print(add_up)
