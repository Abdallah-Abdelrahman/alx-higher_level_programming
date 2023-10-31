#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ((str[i]) >= 'a' and (str[i]) <= 'z'):
            print('{:c}'.format((ord(str[i]) - 32), end=''), end='')
    print()
