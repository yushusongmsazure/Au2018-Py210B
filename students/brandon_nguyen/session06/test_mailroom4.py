#!/usr/bin/env python3
# Week6 Excercise mailroom part 4b- the test file
# Student: Brandon Nguyen - Au2018
import sys
import unittest
from decimal import Decimal
from datetime import datetime
from mailroom4 import sort_sum4_report


def test_sort_sum4_report():
    input_db = {'FirstNameA LastNameA': [1, 1, 1, 1],
                'FirstNameB LastNameB': [2, 2, 2, 2],
                'FirstNameC LastNameC': [3, 3, 3, 3],
                }
    expect_sum_db = [('FirstNameC LastNameC', [12], [4], [3.0]),
                     ('FirstNameB LastNameB', [8], [4], [2.0]),
                     ('FirstNameA LastNameA', [4], [4], [1.0]),
                     ]
    assert sort_sum4_report(input_db) == expect_sum_db
