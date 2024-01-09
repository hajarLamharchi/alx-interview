#!/usr/bin/python3
"""This module defines the function canUnlockAll"""


def canUnlockAll(boxes):
    """This function takes a list of lists as argument
        and every list presents a box containing keys
        that can open other boxes
        and it returns true if all the boxes
        can be opened and false otherwise"""
    """keys = [0]
    canOpen = True
    for box in boxes:
        for key in box:
            keys.append(key)
            if (boxes.index(box) not in keys):
                canOpen = False
    return canOpen"""

    keys = {}
    keysSet = set([0])
    canOpen = True
    for box in boxes:
        keys[boxes.index(box)] = box
    for key, value in keys.items():
        for val in value:
            keysSet.add(val)
            if (key not in keysSet and key in keys[key]):
                canOpen = False
    return canOpen
