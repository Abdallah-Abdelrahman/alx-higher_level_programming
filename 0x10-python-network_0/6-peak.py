#!/usr/bin/python3
'''Module defines `find_peak` function'''


def peak(_list, lo, hi, _len):
    '''Helper function'''
    mid = lo + (hi - lo) // 2

    if (mid == 0 or _list[mid] > _list[mid - 1]) and\
       (mid == _len-1 or _list[mid] > _list[mid+1]):
        return _list[mid]
    if (mid > 0 and _list[mid - 1] > _list[mid]):
        return peak(_list, lo, mid - 1, _len)
    return peak(_list, mid + 1, hi, _len)


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers.'''

    if not list_of_integers:
        return None
    _len = len(list_of_integers)
    if _len == 1:
        return list_of_integers[0]
    return peak(list_of_integers, 0, _len - 1, _len)
