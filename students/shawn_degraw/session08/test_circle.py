"""
test code for circle.py
"""

import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *
from sphere import *


# Step 1 tests

def test_radius():

    c = Circle(5)

    assert(c.radius) == 5


def test_emptycircle():

    c = Circle()

    assert(c.radius) == 0


# Step 2 tests

def test_diameter():

    c = Circle(5)

    assert(c.diameter) == 10


# Step 3 tests

def test_setdiameter():

    c = Circle()
    c.diameter = 6

    assert(c.radius) == 3
    assert(c.diameter) == 6


# Step 4 tests

def test_area():

    c = Circle(2)

    assert(c.area) == 12.566371


def test_setarea():

    c = Circle(2)

    try:
        c.area = 12
    except AttributeError:
        assert(True)
    else:
        assert(False)


# Step 5 tests

def test_diametercontructor():

    c = Circle.from_diameter(8)

    assert(c.radius) == 4
    assert(c.diameter) == 8


# Step 6 tests

def test_repr():

    c = Circle(5)
    d = repr(c)
    assert(d) == 'Circle(5)'


# Step 7 tests ?

def test_add():

    c1 = Circle(5)
    c2 = Circle(3)
    c3 = c1 + c2

    assert(c3.radius) == 8


def test_multiply():

    c1 = Circle(5)

    c3 = c1 * 3

    assert(c3.radius) == 15

    c4 = 2 * c1

    assert(c3.radius) == 10


# Step 8 tests

def test_lessthan():

    c1 = Circle(5)
    c2 = Circle(8)

    assert(c1 < c2) == True
    assert(c2 < c1) == False


def test_greaterthan():

    c1 = Circle(5)
    c2 = Circle(8)

    assert(c1 > c2) == False
    assert(c2 > c1) == True

# Step 8 optional?


# Step 9 tests

def test_sphere():

    s = Sphere(5)

    assert(s.radius) == 5
    assert(s.diameter) == 10
    assert(s.volume) == 523.598776


def test_spherediameter():

    s = Sphere.from_diameter(8)

    assert(s.radius) == 4
    assert(s.diameter) == 8
