#!/usr/bin/python3
"""
Created @ Aug 13
Author James Gatheru
"""


def makeChange(coins, total):
    """
    function to calculate the fewest number
        of coins  needed to meet a given amount total.
    """
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    # Initialize a list to store the minimum coins needed for each amount up
    # to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make a total of 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # if dp[total] is still infinity, it means the totalcannot be met by any
    # combination of coins
    return dp[total] if dp[total] != float('inf') else -1
