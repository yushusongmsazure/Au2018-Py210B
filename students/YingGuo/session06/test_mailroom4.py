#!/usr/bin/env python

"""session06, write test code for mailroom"""

from mailroom4 import report
from mailroom4 import all_letter
from mailroom4 import donor_list

#test donor list in send a thank you func
def test_donor_list():
    data = {"Tom":[100,200], "Tim":[3000]}
    expected = ["Tom", "Tim"]
    actual = donor_list(data)
    assert expected == actual

#test report func
def test_report():
    data = {"Tom":[100,200], "Tim":[3000]}
    expected = [("Tim", 3000, 1, 3000), ("Tom", 300, 2, 150)]
    actual = report(data)
    assert expected == actual

#how to test all_letters func?


