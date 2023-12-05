#!/usr/bin/python3
"""Module defines append_write function"""


def append_write(filename="", text=""):
    """append to file """

    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
