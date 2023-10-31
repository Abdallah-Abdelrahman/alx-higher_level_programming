#!/usr/bin/python3

def pow(a, b):
    tmp = a

    if (b < 0):
        a = 1 / a
        tmp = a
        b = -b
    if (b == 0):
        return (1)
    b -= 1
    while (b):
        a *= tmp
        b -= 1
    return (a)
