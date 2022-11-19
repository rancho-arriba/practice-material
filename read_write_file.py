#!/usr/local/bin/python3

import os

""" Reading from and writing/appending to a file."""

def write_to_file(filename, text):
    """ Write text to the file"""
    with open(filename, 'w', encoding="utf-8") as write_it:
        write_it.write(f'{text}')

write_to_file('greet.txt', '\nHello!\n')

def append_to_file(filename, text):
    """ Append text to the file"""
    with open(filename, 'a', encoding="utf-8") as append_it:
        append_it.write(f'{text}')

append_to_file('greet.txt', '\nGoodbye!\n')

def read_from_file(filename):
    """ Read text from the file"""
    with open(filename, encoding="utf-8") as read_it:
        contents = read_it.read()
        print(f'{contents}')

read_from_file('greet.txt')

os.remove('greet.txt')
