#!/usr/bin/python3
"""
A function that prints a text after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text_indentation - .
    Args:
        text: List of texts.
    Returns:
        new sets of texts.
    """

    if (type(text) != str):
        raise TypeError("text must be a string")
    new = "".join(ch if ch not in '?.:' else ch + "\n\n" for ch in text)
    l_l = new.split('\n')
    new = ""
    for line in l_l:
        new += '\n' + (line.strip())
    new = new[1:]
    print(new, end="")
