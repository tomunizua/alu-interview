#!/usr/bin/python3
'''
Module to calculate retained rainwater in relief map cross-section.
'''

from typing import List

def rain(walls: List[int]) -> int:
    '''
    Calculate total retained rainwater given wall heights.

    Args:
        walls (List[int]): Non-negative integers representing wall heights.

    Returns:
        int: Total retained rainwater.

    Note:
        Ends of the list (before index 0 and after index walls[-1]) do not retain water.
        Returns 0 if the list is empty.
    '''
    
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(n):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water
