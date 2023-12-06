#!/usr/bin/python3
"""Module defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Append new line contains the new string

    for each occurence of `search_string`

    Args:
        filename: name of the file
        search_string: string to search for in a line
        new_string: string to append
    """

    _line = ''
    with open(filename, 'r+') as f:
        for line in f:
            _line += line
            if search_string in line:
                _line += new_string
        f.seek(0)
        f.write(_line)
