#!/usr/bin/python3
"""
Module that defines the function text_indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)
    current_segment = []

    while i < n:
        # Collect characters until a separator is found
        while i < n and text[i] not in ".?:":
            current_segment.append(text[i])
            i += 1

        if i < n and text[i] in ".?:":
            current_segment.append(text[i])
            i += 1
            segment = ''.join(current_segment).strip()
            if segment:
                print(segment)
                # Check if there are more non-space characters ahead
                j = i
                while j < n and text[j] == ' ':
                    j += 1
                if j < n:
                    print('\n', end='')
            current_segment = []
            # Skip spaces after the separator
            while i < n and text[i] == ' ':
                i += 1

    # Print remaining segment without trailing newlines
    if current_segment:
        segment = ''.join(current_segment).strip()
        if segment:
            print(segment, end='')
