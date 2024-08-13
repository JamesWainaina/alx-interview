#!/usr/bin/python3
"""
Created at Aug 13
@Author James Gatheru
"""


def makeChange(coins, total):
    """
    function to calculate the fewest number of coins
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total == 0:
        return count
    else:
        return -1
