#!/usr/bin/python3
"""Module defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Append new line contains the new string

    for each occurence of `search_string`
    """

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if search_string in line:
                line += new_string
