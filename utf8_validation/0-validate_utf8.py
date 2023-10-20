#!/usr/bin/python3
"""
This module contains a function to validate UTF-8 encoding in alist ofintegers
"""


def validUTF8(data):
    number_of_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for number in data:
        mask = mask1
        if number_of_bytes == 0:
            while mask & number:
                number_of_bytes += 1
                mask >>= 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (number & mask1 and not (number & mask2)):
                return False
        number_of_bytes -= 1
    return number_of_bytes == 0
