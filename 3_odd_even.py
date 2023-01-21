#!/usr/local/bin/python3

""" Is input an odd/even number?"""

def isOdd(number):
    """ Return whether number mod 2 is 1:"""
    return number % 2 == 1

def isEven(number):
    """ Return whether number mod 2 is 0:"""
    return number % 2 == 0

assert not isOdd(42)
assert isOdd(9999)
assert not isOdd(-10)
assert isOdd(-11)
assert not isOdd(3.1415)
assert isEven(42)
assert not isEven(9999)
assert isEven(-10)
assert not isEven(-11)
assert not isEven(3.1415)
