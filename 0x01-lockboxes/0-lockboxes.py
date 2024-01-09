#!/usr/bin/python3
"""This module defines the function canUnlockAll"""

def canUnlockAll(boxes):
    """This function takes a list of lists as argument
        and every list presents a box containing keys that can open other boxes
        and it returns true if all the boxes can be opened and false otherwise"""
    
    keys = [0]
    canOpen = True
    for box in boxes:
        for key in box:
            keys.append(key)
            if (boxes.index(box) not in keys):
                canOpen = False
    return canOpen
