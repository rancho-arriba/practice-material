#!/usr/local/bin/python3

"""Temperature conversion"""
cel = input('Enter degrees Celsius to convert to Fahrenheit: ')

def convert_c2f():
    """Celsius to Fahrenheit"""
    degrees_f = (int(cel) * (9 / 5)) + 32
    print(f'{cel} degrees Celsius is about {degrees_f} degrees Fahrenheit.')
convert_c2f()
