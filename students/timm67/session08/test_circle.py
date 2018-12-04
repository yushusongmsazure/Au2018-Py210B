#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Circle Tests
"""

import pytest
import math
from circle import Circle

test_radius_int = 4
test_radius = float(4)
test_diameter = test_radius * float(2)
test_circum = float(2.0) * math.pi * test_radius
test_area = math.pi * (test_radius ** 2)

def test_circle_init_methods():
    c = Circle(test_radius_int)
    assert(c.radius == test_radius)
    assert(c.diameter == test_diameter)
    assert(c.circumference == test_circum)
    assert(c.area == test_area)

# def test_circle_alt_const():
#     c2 = Circle.from_diameter(test_diameter)
#     assert(c2.radius == test_radius)
#     assert(c2.diameter == test_diameter)
#     assert(c2.circumference == test_circum)
#     assert(c2.area == test_area)

