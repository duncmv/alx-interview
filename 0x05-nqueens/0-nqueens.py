#!/usr/bin/python3
"""a program that solves the N queens problem.

    Usage: nqueens N
        If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number
         and exit with the status 1
        If N is smaller than 4, print N must be at least 4
        and exit with the status 1
"""
import sys


av = sys.argv
if len(av) != 2:
    print("Usage: nqueens N")
    exit(1)
if av[1].isdigit() is False:
    print("N must be a number")
    exit(1)
if int(av[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(av[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """ solve n queens problem """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
