#!/usr/bin/python3
"""Module defines load_from_json_file function"""

from json import dumps


def load_from_json_file(filename):
    """Dserialize obj from a file"""

    with open(filename, 'r', encoding='utf-8') as f:
        return dumps(f.read())
