#!/usr/bin/python3
"""
Defines a function that calculates how much rainwater will be retained
given a list of non-negative integers that represents walls of width 1
"""


def rain(walls):
    """
    Calculates rainwater retention given list representing walls
    parameters:
        walls: represents walls of width 1
    returns:
        [int]: representing the total amount of rainwater retained
    """
    if type(walls) is not list or walls is []:
        return 0
    for i in walls:
        if i < 0:
            return 0
    amount = 0
    for i, height in enumerate(walls):
        left_max = max(walls[:i + 1])
        right_max = max(walls[i:])
        shorter_wall = min(left_max, right_max)
        amount += max(shorter_wall - height, 0)
    return amount
