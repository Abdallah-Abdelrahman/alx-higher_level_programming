#!/usr/bin/python3

"""This module defines text_indentation function."""


def text_indentation(text):
    """Outputs a text.

     with 2 new lines after each of these characters: ., ? and :
     There should be no space at the beginning,
     or at the end of each printed line

    Args:
        text(str): text to parse

    Raises:
        TypeError: text is not a string
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    parsed = ''
    i = 0

    for char in text:
        if i and parsed[i - 1] == '\n' and char == ' ':
            continue
        parsed += char
        i += 1
        if char in ('.', ':', '?'):
            parsed += '\n\n'
            i += 2

    print(parsed)
