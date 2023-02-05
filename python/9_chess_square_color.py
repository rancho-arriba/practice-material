#!/usr/local/bin/python3

""" What color is the chessboard square?"""

def get_square_color(column, row):
    """ Using modulo to return black, white, or blank string."""
    if column <1 or column > 8 or row <1 or row >8:
        return ""
    if column % 2 == row %2:
        return "white"
    else:
        return "black"


assert get_square_color(1, 1) == 'white'
assert get_square_color(2, 1) == 'black'
assert get_square_color(1, 2) == 'black'
assert get_square_color(8, 8) == 'white'
assert get_square_color(0, 8) == ''
assert get_square_color(2, 9) == ''
