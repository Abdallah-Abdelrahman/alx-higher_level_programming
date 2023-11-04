#!/usr/bin/python3

def max_integer(my_list=[]):
    _max = None
    length = len(my_list)

    if (not length):
        return _max
    if (length == 1):
        return my_list[0]
    _max = my_list[0]
    for i in range(length):
        for num in my_list[i + 1:]:
            if (num > _max):
                _max = num
    return _max
