#!/usr/bin/python3

import hidden_4

if (__name__ == '__main__'):
    names = dir(hidden_4)
    for str in names:
        if (str.startswith('__')):
            continue
        print(str)
