#!/usr/bin/env python3
# Week6 Excercise mailroom part 4b- the test file
# Student: Brandon Nguyen - Au2018
import sys
import unittest
from decimal import Decimal
from datetime import datetime
from mailroom4 import sort_sum4_report
from mailroom4 import update_donation


input_db = {'FirstNameA LastNameA': [1, 1, 1, 11],
            'FirstNameB LastNameB': [2, 2, 2, 22],
            'FirstNameC LastNameC': [3, 3, 3, 33],
            }

TEST_LETTER = "\n".join(("", "Dear {Name},", "", "Thank you for your "
                         "kind donation of {LastAmnt:.2f}.",
                         "It will be put to very good use.", "",
                         "Sincerely, ", "", "-The Team\n"))


# Test 1: the sum list and sort for report in mailroom
def test_sort_sum4_report():
    expect_sum_db = [('FirstNameC LastNameC', [42], [4], [10.5]),
                     ('FirstNameB LastNameB', [28], [4], [7.0]),
                     ('FirstNameA LastNameA', [14], [4], [3.5]),
                     ]
    assert sort_sum4_report(input_db) == expect_sum_db


# Test 2: update_donation
def test_update_donation():
    empty_dict = {}
    input_list = ['First Last', 50]
    expected_test1 = {'First Last': [50]}
    # test empty dict
    assert update_donation(input_list, empty_dict) == expected_test1  
    # test existing dict
