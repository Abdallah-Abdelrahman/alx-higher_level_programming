#!/usr/bin/python3
"""Module defines save_to_json_file function"""

from json import dumps


def save_to_json_file(my_obj, filename):
    """Write serialized pyhton obj to a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
