#!/usr/bin/env python3

import pytest
from donor_models import Donor
from donor_models import DonorCollection

def test_donor_class():
    d = Donor('Ryan Seacrest', 1000)
    assert d.name == 'Ryan Seacrest'
    assert d.donations[0] == 1000
    assert d.total_donations == 1000

def test_DonorCollection_class():
    dc = DonorCollection()
    dc.add_new_donor('Bill Gates')
    with pytest.raises(ValueError):
        dc.add_new_donor('Bill Gates')
    dc.add_donation('Bill Gates', 1234)
    d = dc.get_donor('Bill Gates')
    assert d.num_donations == 1
    assert d.total_donations == 1234
    assert d.name == 'Bill Gates'