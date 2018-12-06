#!/usr/bin/env python3

"""session09, assignment oo mailroom, Rachel Schirra"""

class Donor():
    def __init__(self, donor_name, initial_donation=None):
        self.__name = donor_name
        self.__donations = []
        if initial_donation:
            self.add_donation(initial_donation)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def donations(self):
        return self.__donations
    
    @property
    def count_donations(self):
        return len(self.__donations)
    
    @property
    def total_donations(self):
        return sum(self.__donations)
    
    @property
    def latest_donation(self):
        return self.__donations[-1]
    
    @property
    def avg_donation(self):
        return self.total_donations / self.count_donations
    
    def __str__(self):
        return "Donor name: {}\nDonations: {}".format(self.__name, 
            self.__donations)
    
    def add_donation(self, donation):
        self.__donations.append(float(donation)) # If not floatable throw error
    
    def generate_letter(self):
        pass
    
    def generate_report_row(self):
        pass


class DonorCollection():
    def __init__(self):
        self.__donors = {} # name: Donor pairs
    
    def add_new_donor(self, name, donor):
        if name in self.__donors:
            raise ValueError('Name ({}) already exists.'.format(name))
        self.__donors[name] == Donor(name)
    
    def get_donor(self, name):
        return self.__donors[name]

    def generate_report(self):
        pass
    
    def generate_all_letters(self, folder):
        pass
    
    
if __name__ == '__main__':
    dc = DonorCollection()