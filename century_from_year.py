#!/usr/local/bin/python3

"""Given a year, return the century it is in."""

def century(year):
    if (year % 100) == 0:
        return year // 100
    else:
        return year // 100 + 1

year = 2015
# year = int(input('Enter the year:  '))
print(f'Year:  {year}.  Century:  {century(year)}.')
