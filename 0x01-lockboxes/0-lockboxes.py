#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    box_number = len(boxes)
    if box_number < 2:
        return True
    keys = set(boxes[0]) | {0}
    open = {0}
    while open != set(range(box_number)):
        next_open = set()
        for i in keys:
            if i < box_number:
                next_open |= set(boxes[i])
        keys |= next_open
        keys = {x for x in keys if x < box_number}
        if not keys - open:
            return False
        open |= keys
    return True
