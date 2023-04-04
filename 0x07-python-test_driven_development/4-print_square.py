#!/usr/bin/python3
"""
A function that prints a square with the character #.
"""


def print_square(size):
    """
    print_square - Function that prints a square with # character.
    Args:
        size: An integer with the size of the square.
    Returns:
        Nothing
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for j in range(size):
        for k in range(size):
            print("#", end="")
        print()
