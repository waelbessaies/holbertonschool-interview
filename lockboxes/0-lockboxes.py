#!/usr/bin/python3
"""
    lockboxes
"""

def canUnlockAll(boxes):
    list = [0]

    for key in list:
        for src in boxes[key]:
            if src not in list and src < len(boxes):
                list.append(src)
    
    for index in range(len(boxes)):
        if index not in list:
            return False
    
    return True
