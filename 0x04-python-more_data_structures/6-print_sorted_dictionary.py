#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        print('{0}: {1}'.format(k, a_dictionary[k]))
