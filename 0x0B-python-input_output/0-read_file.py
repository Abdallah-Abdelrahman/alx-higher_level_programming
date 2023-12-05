#!/usr/bin/python3
""" Module define read_file ``function``"""


def read_file(filename=""):
    """read file and output it"""
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read())
