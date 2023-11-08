#!/usr/bin/python3

from functools import reduce


def uniq_add(my_list=[]):
    return reduce(lambda acc, curr: acc + curr, set(my_list))
