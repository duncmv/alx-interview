#!/usr/bin/python3
"""
Making Change"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total

    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1

coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        total = total % coin
        if total == 0:
            return count
    if total != 0:
        return -1
