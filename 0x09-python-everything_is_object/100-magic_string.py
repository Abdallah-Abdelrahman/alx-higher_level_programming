#!/usr/bin/python3
def magic_string():
    magic_string.i = getattr(magic_string, 'i', 0) + 1
    return ', '.join(['BestSchool' for _ in range(magic_string.i)])
