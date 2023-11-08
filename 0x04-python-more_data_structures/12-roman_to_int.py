#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }

    if isinstance(roman_string, str):
        # "IX"
        for i, letter in enumerate(roman_string):
            if (not i):
                num += roman_num[letter]
            else:
                prev_num = roman_num[roman_string[i - 1]]
                curr_num = roman_num[letter]
                num += curr_num - prev_num - prev_num\
                    if prev_num < curr_num else curr_num
    return num
