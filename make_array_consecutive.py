#!/bin/env python3

def makeArrayConsecutive(statues):
    oscar = 0
    statues.sort()
    for i in range(0, len(statues) -1):
        if statues[i + 1] - statues[i] > 1:
            oscar += statues[i + 1] - statues[i] - 1
    return oscar

statues = [3, ]
