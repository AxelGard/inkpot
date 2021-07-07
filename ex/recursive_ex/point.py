
from math import sqrt


class Point:
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x_init, y_init):
        '''Defines x and y variables'''
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        '''Determines where x and y move'''
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])
