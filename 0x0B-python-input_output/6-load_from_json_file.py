#!/usr/bin/python3
"""Module defines load_from_json_file function"""

from json import loads


def load_from_json_file(filename):
    """Dserialize obj from a file"""

    with open(filename, 'r', encoding='utf-8') as f:
        return loads(f.read())
