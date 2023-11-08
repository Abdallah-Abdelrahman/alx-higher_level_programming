#!/usr/bin/python3

from functools import reduce


def uniq_add(my_list=[]):
    unique_list = []

    for elem in my_list:
        if elem not in unique_list:
            unique_list.append(elem)

    return (reduce(lambda acc, curr: acc + curr, unique_list))
