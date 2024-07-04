#!/usr/bin/python3
""" Module that checks locked boxes """


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of list of int): A list of boxes, each
    containing a list of keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set([0])  # Start with the first box opened
    keys = set(boxes[0])  # Start with keys from the first box

    # While there are keys to use
    while keys:
        key = keys.pop()
        if key < n and key not in opened:
            opened.add(key)  # Mark this box as opened
            keys.update(boxes[key])  # Add new keys from the newly opened box

    # Check if we have opened all boxes
    return len(opened) == n
