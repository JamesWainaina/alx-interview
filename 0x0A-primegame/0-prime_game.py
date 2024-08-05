#!/usr/bin/python3


"""
Date Aug 5
@Author: James Gatheru
"""


def SieveEratoshenes(n):
    """
    Function to sieve all prime numbers
    """
    prime = [True for i in range(n + 1)]
    p = 2
    while(p * p <= n):
        if (prime[p]):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    prime_num = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_num.append(p)
    return prime_num


def isWinner(x, nums):
    """
    function to calculate the winner
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_numbers = SieveEratoshenes(n)
        prime_count = len(prime_numbers)

        # Determine the winner based on the prime count
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
