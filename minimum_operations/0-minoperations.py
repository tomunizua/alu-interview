#!/usr/bin/python3

    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve the target, or 0 if impossible.
    """

def minOperations(n):

    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    current = 1

    while current < n:
        if n % current == 0:
            clipboard = current
            operations += 2  # Copy All and Paste
            current *= 2
        else:
            clipboard += current
            operations += 1  # Paste
            current += clipboard

    return operations


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

