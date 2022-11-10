#!/usr/local/bin/python3

""" Calculate area, surface area, and volume."""

def area(length, width):
    """ Surface area of one plane."""
    return length * width

def perimeter(length, width):
    """ Perimeter of a cube or cuboid."""
    return (length * 2) + (width * 2)

def surface_area(length, width, height):
    """ Surface area of a cube or cuboid."""
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

def volume(length, width, height):
    """ Volume of a cube or cuboid."""
    return length * width * height

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surface_area(10, 10, 10) == 600
assert surface_area(9999, 0, 9999) == 199960002
assert surface_area(5, 8, 10) == 340
