#!/bin/env python3

def solution(n):
    if n >= 10**4 or n < 1:
        return False
    return n**2+(n-1)**2

print(solution(4))
print(solution(3))
print(solution(2))