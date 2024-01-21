#!/usr/bin/python3
"""
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve the target, or 0 if impossible.
"""

def minOperations(n):

if n < 2:
        return 0

    current_num_of_h = 1
    copied = 0
    num_of_operations = 0

    while current_num_of_h < n:
        if n % current_num_of_h == 0:
            copied = current_num_of_h
            num_of_operations += 1

        current_num_of_h += copied
        num_of_operations += 1
    return num_of_operations
