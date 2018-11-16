#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Mailroom Part 4 assignment
"""

import pytest
from mailroom_part4 import create_report_task
from mailroom_part4 import send_thankyou_multiple_donors_task
from mailroom_part4 import test_send_thankyou_single_donor_task
from pathlib import Path

thankyou_filelist = []

def test_report():
    outlines = create_report_task()
    assert(5 == len(outlines))

def test_thankyou_files():
    global thankyou_file_list
    thankyou_filelist = send_thankyou_multiple_donors_task()
    for test_file in thankyou_filelist:
        try:
            test_file_path = Path(test_file)
            assert(test_file_path.is_file())
        except FileNotFoundError:
            assert(False)

def test_single_thankyou():
    test_donor = {('Jim', 'Smith'): [50.0, 100.0]}
    thankyou_lines = test_send_thankyou_single_donor_task(test_donor)
    assert 'Jim' in thankyou_lines[0]
    assert '100.00' in thankyou_lines[1]
    assert '150.00' in thankyou_lines[2]
    assert '75.00' in thankyou_lines[2]




