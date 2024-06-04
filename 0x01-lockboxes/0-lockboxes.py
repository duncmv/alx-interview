#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    box_number = len(boxes)
    if box_number < 2:
        return True
    keys = set(boxes[0])
    open = set([0])
    if 1 not in keys:
        return False
    while True:
        if len(open) == box_number:
            return True
        for i in open:
            open = open.union(set(boxes[i]))
            keys = keys.union(set(boxes[i]))
        open = open.difference(keys)
        if not open:
            return False
