#!/usr/bin/python3
"""Module defines write_file function"""


def write_file(filename="", text=""):
    """overwrite file"""

    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
