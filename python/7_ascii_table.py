#!/usr/local/bin/python3

""" Return the ASCII number and its corresponding text character."""

def ascii_table():
    """ Between 32 and 126."""
    for num in range(32, 127):
        print(num, chr(num))

ascii_table()
