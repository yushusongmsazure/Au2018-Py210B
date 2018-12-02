"""
test code for circle.py
"""

import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *


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
