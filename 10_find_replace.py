#!/usr/local/bin/python3

""" Find and replace function."""

def find_replace(text, old_text, new_text):
    """ The function itself."""
    replaced_text = ''
    i = text[0:-1]
    

assert find_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_replace('fox', 'fox', 'dog') == 'dog'
assert find_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
