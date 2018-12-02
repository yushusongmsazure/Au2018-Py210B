#!/usr/bin/env python3

"""
Class to implement simple circle

"""

from math import pi


class Circle:

    def __init__(self, init_radius=0):
            self.radius = init_radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return round(pi * self.radius ** 2, 6)
