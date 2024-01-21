#!/usr/bin/python3
def min_operations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve the target, or 0 if impossible.
    """
    # Check if n is less than or equal to 1, in which case it's impossible.
    if n <= 1:
        return 0

    # Initialize variables for clipboard and current count.
    operations = 0
    clipboard = 1
    current = 1

    # Perform operations until the target count is reached.
    while current < n:
        # If n is divisible by current, perform a Copy All and Paste operation.
        if n % current == 0:
            clipboard = current
            operations += 2  # Copy All and Paste
            current += clipboard
        else:
            # If n is not divisible, increment current by 1.
            operations += 1  # Paste
            current += 1

    # Return the total number of operations.
    return operations


if __name__ == "__main__":
    # Example usage and output.
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, min_operations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, min_operations(n)))
