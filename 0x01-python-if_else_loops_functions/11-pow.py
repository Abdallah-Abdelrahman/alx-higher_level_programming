#!/usr/bin/python3

def pow(a, b):
    tmp = a

    if (b < 0):
        b = -b
    if (b == 0):
        return (1)
    b -= 1
    while (b):
        a *= tmp
        b -= 1
    return (a if b > 0 else 1 / a)
