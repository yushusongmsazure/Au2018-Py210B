"""
test code for circle.py
"""

import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *


#Step 1 tests

def test_radius():

    c = Circle(5)

    assert(c.radius) == 5


def test_zeroradius():

    try:
        badc = Circle(0)
    except ValueError:
        assert(True)
    else:
        assert(False)


def test_stringradius():

    try:
        badc = Circle('test')
    except TypeError:
        assert(True)
    else:
        assert(False)


# Step 2 tests

def test_diameter():

    c = Circle(5)

    assert(c.diameter) == 10