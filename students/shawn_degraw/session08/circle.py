#!/usr/bin/env python3

"""
Class to implement simple circle

"""


class Circle:

    def __init__(self, init_radius):
        if not init_radius:
            raise ValueError
        elif type(init_radius) != int and type(init_radius) != float:
            raise TypeError
        else:
            self.radius = init_radius

    @property
    def diameter(self):
        return 2 * self.radius
