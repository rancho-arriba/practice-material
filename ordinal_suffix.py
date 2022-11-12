#!/usr/local/bin/python3

""" Return the given number with its ordinal suffix (_st, _nd, _rd, _th). """

def ordinal_suffix(number):
    """ Use string slicing to determine last one or two digits."""
    number_string = str(number)
    if number_string[-2:] in ('11', '12', '13'):
        return number_string+'th'
    elif number_string[-1:] == '1':
        return number_string+'st'
    elif number_string[-1:] == '2':
        return number_string+'nd'
    elif number_string[-1:] == '3':
        return number_string+'rd'
    else:
        return number_string+'th'

print(ordinal_suffix(956))
