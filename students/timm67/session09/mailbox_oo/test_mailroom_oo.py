import pytest
from donor_models import Donor

def test_donor_class():
    d = Donor('Ryan Crest', 1000)
    assert d.name == 'Ryan Seacrest'
    assert d.donations[0] == 1000