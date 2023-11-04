#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        return [my_list[x] % 2 == 0 for x in range(len(my_list))]
