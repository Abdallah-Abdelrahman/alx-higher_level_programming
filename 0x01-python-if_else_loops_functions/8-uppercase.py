#!/usr/bin/python3

def uppercase(str):
    fmt = ''

    for i in range(len(str)):
        lower = str[i] >= 'a' and (str[i]) <= 'z'
        if (lower):
            fmt += '{:c}'.format(ord(str[i]))
        else:
            fmt += str[i]
    print(fmt)
