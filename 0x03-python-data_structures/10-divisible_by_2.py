#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if (not my_list or not len(my_list)):
        return my_list
    return [x % 2 == 0 for x in range(len(my_list))]
