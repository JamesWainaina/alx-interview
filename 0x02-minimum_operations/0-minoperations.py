#!/usr/bin/python3
"""Minimum operations to a function"""


def minOperations(n):
    """function to calculate the minimum operations for copying and pasting"""
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
