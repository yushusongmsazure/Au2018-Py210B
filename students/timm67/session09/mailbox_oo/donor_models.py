#!/usr/bin/env python3

class Donor:
    """
    Donor class
    """
    def __init__(self, name, initial_donation=None):
        self._name = name
        self._donations = []
        if initial_donation is not None:
            self._donations.append(initial_donation)

    def __str__(self):
        return "Donor: name={}, donations={}".format(self._name, self._donations)

    def add_donation(self, donation):
        self._donations.append(donation)

    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations


