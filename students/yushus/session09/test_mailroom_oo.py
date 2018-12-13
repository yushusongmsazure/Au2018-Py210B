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

    dc.add_donation('Bill Gates', 100)

    print(dc.get_donor('Bill Gates')
    print(Donor("Bill Gates", 100))

    assert print(dc.get_donor('Bill Gates')) == '[Donor name=Bill Gates, donations=[100]]'
