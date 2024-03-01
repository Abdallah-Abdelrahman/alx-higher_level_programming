#!/usr/bin/python3
'''Module defines `find_peak` function'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers.'''

    if not list_of_integers:
        return None
    _len = len(list_of_integers)
    if _len == 1:
        return list_of_integers[0]
    # check for every other element
    for i in range(1, _len - 1):
        # check if the neighbors are smaller
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
