#!/usr/bin/env python

"""
Class: Python 210 B, Au2018
Exercise: Session 06, Mailroom Part 04 Unit Test
Student: Jason Jakubiak
"""
from mailroom04 import *
import mailroom04
import os.path

test_name = "Name"
test_amt = 9999

test_sort_input = [
    ('A', 3),
    ('B', 1),  
    ('C', 2),
    ('D', 4),
    ]

test_sort_output = [
    ('D', 4),
    ('A', 3),
    ('C', 2),
    ('B', 1),
    ]

test_db_input = {
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30],
    "C": [9, 8, 7, 6],
    "D": [100.5, 50.25, 75.55, 25.45, 200.25],
    }

test_db_output = [
    ('D', 452, 5, 90.4),
    ('B', 60, 3, 20),  
    ('C', 30, 4, 7.5),
    ('A', 15, 5, 3),
    ]


def test_create_msg():
    assert mailroom04.create_msg(test_name,test_amt) == \
        thanks_txt.format(test_name,test_amt)


def test_donor_sort():
    assert mailroom04.donor_sort(test_sort_input) == test_sort_output


def test_donor_calc():
    assert mailroom04.donor_calc(test_db_input) == test_db_output


def test_write_letter():
    mailroom04.write_letter("")
    donor_list = [donor.capitalize() for donor, key in donor_db.items()]

    for name in donor_list:
        path = name + ".txt"
        assert os.path.exists(path)
