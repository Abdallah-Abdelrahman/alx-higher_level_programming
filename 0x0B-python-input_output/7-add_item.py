#!/usr/bin/python3
"""Module read args from command-line.

append serialized arguments to file ``add_item.json``

Attributes:
    file_name: json file to write and read form
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    file_name = 'add_item.json'

    try:
        _list = load_from_json_file(file_name)
    except Exception:
        _list = []

    _list.extend([argv[i] for i in range(1, len(argv))])
    save_to_json_file(_list, file_name)
