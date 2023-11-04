#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    for c in my_string:
        new_str += c if c != 'c' and c != 'C' else ''
    return (new_str)
