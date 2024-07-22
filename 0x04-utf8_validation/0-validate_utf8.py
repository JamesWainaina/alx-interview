#!/usr/bin/python3

"""
Created at Mon July 22 2024
@Author: James Gatheru
"""


def validUTF8(data):
    """
    Determines if a given data ste is valid UTF-8
    """
    num_of_bytes = 0

    for byte in data:
        if num_of_bytes == 0:
            if byte < 128:
                continue

            if 192 <= byte < 224:
                num_of_bytes = 1
            elif 224 <= byte < 240:
                num_of_bytes = 2
            elif 240 < byte < 248:
                num_of_bytes = 3
            else:
                return False
        else:
            if 128 <= byte < 192:
                num_of_bytes -= 1
            else:
                return False
    return True
