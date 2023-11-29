#!/usr/bin/python3
"""Module"""


def magic_string():
    """output"""
    magic_string.i = getattr(magic_string, 'i', 0) + 1
    _str = ''

    for j in range(magic_string.i):
        _str += 'BestSchool' + ('', ', ')[j < magic_string.i - 1]
    return _str
