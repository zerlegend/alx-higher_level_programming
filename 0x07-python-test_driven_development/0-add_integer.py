#!/usr/bin/python3
"""
Write a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    add_integer - function to add two integers.
    Args:
        a: First number to be added.
        b: Second number to be added.
    Returns:
        The sum of a and b.
    """
    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")
    if ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
