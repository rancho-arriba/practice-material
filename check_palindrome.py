#!/bin/env python3

def solution(inputString):
    backwards = ''.join(reversed(inputString))
    if backwards == inputString:
        return True
    return False

inputString = 'tacocat'
answer = solution(inputString)

if answer:
    print(f'{inputString} is a palindrome.')
else:
    print(f'{inputString} is not a palindrome.')
