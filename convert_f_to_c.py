#!/usr/local/bin/python3

"""Temperature conversion"""

fahr = input('Enter degrees Fahrenheit to convert to Celsius: ')

def convert_f2c():
    """Fahrenheit to Celsius"""
    degrees_c = (int(fahr) - 32) * (5 / 9)
    print(f'{fahr} degrees Fahrenheit is about {degrees_c} degrees Celsius')
convert_f2c()
