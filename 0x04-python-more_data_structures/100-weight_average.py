#!/usr/bin/python3

def weight_average(my_list=[]):
    dividend = 0
    divisor = 0

    if not my_list:
        return 0

    for tup in my_list:
        dividend += tup[0] * tup[1]
        divisor += tup[1]

    return dividend / divisor
