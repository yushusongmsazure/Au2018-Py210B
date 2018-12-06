#!/usr/bin/env python3

"""session09, assignment oo mailroom, Rachel Schirra"""

import pytest
from donor_models import *

def test_donor_class():
    d = Donor('Plum', 1700)
    assert d.name == 'Plum'
    assert d.donations == [1700]

    d = Donor('Jelly Kid')
    assert d.name == 'Jelly Kid'
    assert d.donations == []

def test_add_donation():
    d = Donor('Jelly Kid')
    d.add_donation(1)
    assert d.donations == [1]
    d.add_donation(2)
    d.add_donation(3)
    assert d.donations == [1, 2, 3]
    with pytest.raises(ValueError):
        d.add_donation('pineapple')

def test_donor_params():
    d = Donor('Jelly Kid')
    d.add_donation(1)
    d.add_donation(2)
    d.add_donation(3)
    assert d.total_donations == 6
    assert d.avg_donation == 2
    assert d.count_donations == 3
    assert d.latest_donation == 3
