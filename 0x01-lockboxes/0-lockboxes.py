#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
  """determines if all the boxes can be opened"""
  box_number = len(boxes)
  if box_number < 2:
    return True
  keys = boxes[0]
  if 1 not in keys:
    return False
  for i in range(1, box_number - 1):
    keys.extend(boxes[i])
    if i + 1 not in keys:
      return False
  return True