#! usr/bin/env phtyon

""" Circle class assignment by
Arun Nalla 12/08/2018"""

from math import pi
import random

class Circle():

    def __init__(self, radius):
        if radius >= 1:
            self.radius = radius
        else:
            raise ValueError ('Value is less than or equal to zero')

    @property
    def diameter(self):
        self.diameter = self.radius * 2
        return self.radius
 
    @ diameter.setter
    def diameter (self, set_diameter):
        self.radius = set_diameter / 2

    @property
    def area (self):
        return pi * (self.radius ** 2)
    
    @classmethod
    def from_diameter (cls, diameter):
        from_radius = diameter / 2
        return cls(from_radius)

    def __str__ (self):
        return 'Circle with radius {}'.format (self.radius)
    def __repr__(self):
        return 'Circle ({})'.format (self.radius)
    def __add__ (self, other):
        return Circle(self.radius + other.radius)
    def __mul__ (self, other):
        return Circle (self.radius * other)
    def __ls__ (self, other):
        return self.radius < other.radius
    def __le__ (self, other):
        return self.radius <=other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def __eq__(self, other):
        return self.radius == other.radius

class Sphere(Circle):
        def __inti__(self):
            super().__inti__()
        
        def __str__(self):
            return ('Sphere with radius {}'.format(self.radius))

        def __repr__(self):
            return ('Sphere ({})'.format(self.radius))
        
        @property
        def volume (self):
            return (4/3*pi*self.radius**3)

        def area (self):
            raise NotImplementedError

"""
#print methods to confirms

c = Circle(2)

print (c.diameter, c.radius)
print (c.area)

c.diameter = 2
print (c.diameter, c.radius)
print (c.area)

c= Circle(42)

print (c.area)

#c.area = 42
#print (c.area)

c = Circle.from_diameter(8)
print (c.diameter)

print (c.radius)
print (c)
print (repr(c))

c1 = Circle(2)
c2 = Circle (4)

print (c1+c2)

print (c2 * 4)
print (c1 > c2)
print (c1 < c2)
print (c1 == c2)

c3 = Circle(4)
print (c2 == c3)
circles = [Circle(radii) for radii in range(1, 10)]
#for radii in range(1, 10):
#    circles.append(Circle(radii))
print (circles)

circles.sort()
print (circles)

s = Sphere(3)
print (s)
print (repr(s))
print (s.volume)"""


