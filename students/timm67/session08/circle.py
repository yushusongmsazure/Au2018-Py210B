#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Circle Lab
"""

import math

class Circle():
    _radius = float(0.0)
    _diameter = float(0.0)
    _area = float(0.0)
    _circumference = float(0.0)

    def __init__(self, radius):
        self._radius = float(radius)
        self._diameter = float(2.0) * self._radius
        self._area = math.pi * (self._radius ** 2)
        self._circumference = float(2.0) * math.pi * self._radius

    @classmethod
    def from_diameter(self, dia):
        radius = dia // 2
        return Circle(radius)

    def __str__(self):
        return "Circle with radius [{%f}]".format(self._radius)

    def __repl__(self):
        return "Circle({%d})".format(int(self._radius))

    def __add__(self, other):
        return Circle(self._radius + other.radius)

    def __mult__(self, other):
        return Circle(self._radius * float(other))

    def __eq__(self, other):
        return self._radius == other.radius

    def __lt__(self, other):
        return self._radius < other.radius


#
# Properties
#

    @property
    def radius(self):
        print("in radius getter")
        return self._radius

    @property
    def diameter(self):
        print("in diameter getter")
        return self._diameter

    @diameter.setter
    def diameter(self, dia):
        print("in diameter setter", dia)
        self._diameter = float(dia)
        self._radius = self._diameter / float(2.0)
        self._area = math.pi * (self._radius ** 2)
        self._circumference = float(2.0) * math.pi * self._radius

    @property
    def area(self):
        print("in area getter")
        return self._area

    @property
    def circumference(self):
        print("in circumferenc de getter")
        return self._circumference
