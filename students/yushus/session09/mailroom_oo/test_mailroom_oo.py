#!/usr/bin/env/python3

"""
Yushu Song
Au2018-Py210B
Mailroom OO assignment
"""

from donor_models import *
import pytest

def test_donor_class():
    d = Donor('Bill Gates', 1000)

    assert d.name == 'Bill Gates'
    assert d.donations == [1000]
    assert d.total_donations == 1000
    assert d.avg_donations == 1000
    assert d.num_donations == 1

def test_DonorCollection_class():
    dc = DonorCollection()
    dc.add_new_donor('Bill Gates')
    with pytest.raises(ValueError):
        dc.add_new_donor('Bill Gates')

def test_DonorCollection_report():
    dc = DonorCollection()
    dc.add_new_donor("Wei Li")
    dc.add_donation("Wei Li", 100)
    assert "Wei Li" in dc.generate_report()

def test_DonorCollection_property():
    dc = DonorCollection()
    dc.add_new_donor("Wei Li")
    dc.add_donation("Wei Li", 100)
    assert dc.get_donor("Wei Li").donations[-1] == 100

def test_DonorCollection_sort_donors():
    dc = DonorCollection()
    dc.add_new_donor("Wei Li")
    dc.add_donation("Wei Li", 100)
    dc.add_new_donor("Yushu Song")
    dc.add_donation("Yushu Song", 500)
    sorted_donors = dc.sort_donors()
    assert sorted_donors[0].name == "Yushu Song"

def test_DonorCollection_get_donor_names():
    dc = DonorCollection()
    dc.add_new_donor("Wei Li")
    dc.add_donation("Wei Li", 100)
    dc.add_new_donor("Yushu Song")
    dc.add_donation("Yushu Song", 500)
    assert "Yushu Song" in dc.get_donor_names()
    assert "Wei Li" in dc.get_donor_names()