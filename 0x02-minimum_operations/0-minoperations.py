#!/usr/bin/python3
"""findin minumum operations"""


def minOperations(n):
    """findin minumum operations"""
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
