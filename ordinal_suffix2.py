#!/usr/local/bin/python3

""" Return the given number with its ordinal suffix (_st, _nd, _rd, _th). """

def ordinal_suffix2(number):
    """ Use modulo method to determine last one or two digits."""
    
    if number % 100 in ('11', '12', '13'):
        return str(number)+'th'
    elif number % 10 == 1:
        return str(number)+'st'
    elif number % 10 == 2:
        return str(number)+'nd'
    elif number % 10 == 3:
        return str(number)+'rd'
    else:
        return str(number)+'th'

print(ordinal_suffix2(991))
