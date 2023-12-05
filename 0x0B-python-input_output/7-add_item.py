#!/usr/bin/python3
"""Module read args from command-line.

append serialized arguments to file ``add_item.json``

Attributes:
    file_name: json file to write and read form
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = 'add_item.json'

with open(file_name, 'rb+') as f:
    argc = len(argv)
    _list = f.read()

    if _list:
        _list = load_from_json_file(file_name)
    if not isinstance(_list, list):
        save_to_json_file([], file_name)
        _list = load_from_json_file(file_name)
    if argc > 1:
        for i in range(1, argc):
            _list.append(argv[i])
            save_to_json_file(_list, file_name)
