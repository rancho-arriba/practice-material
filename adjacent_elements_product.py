#!/bin/env python3

def solution(inputArray):
    return max(a*b for a, b in zip(inputArray, inputArray[1:]))

nums = [3, 9, -2, -5, 7, 3]

print(f'The largest product of the pair of adjacent elements is {solution(nums)}.')
