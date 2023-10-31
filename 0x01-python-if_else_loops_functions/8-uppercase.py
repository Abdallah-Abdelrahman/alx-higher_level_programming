#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ((str[i]) >= 'a' and (str[i]) <= 'z'):
            print(chr(ord(str[i]) - 32), end='')
    print()
