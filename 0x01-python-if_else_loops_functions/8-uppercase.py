#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        lower = str[i] >= 'a' and (str[i]) <= 'z'
        print('{:c}'.format((ord(str[i]) - 32)) if lower else '{:s}'.format(str[i]), end='')
    print()
