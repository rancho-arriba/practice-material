#!/usr/local/bin/python3

""" A variation on the classic FizzBuzz exercise."""

def fizz_buzz(up_to):
    """ Prints Fizz, Buzz, FizzBuzz, or the number given as variable 'up_to'. """

    for number in range(1, up_to + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")

fizz_buzz(17)
