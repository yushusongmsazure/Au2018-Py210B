#!/usr/bin/env/python3

"""
Yushu Song
Au2018-Py210B
Mailroom OO assignment
"""

import os
import random
import re
import sys

class Donor:
    def __init__(self, name, initial_donation=None):
        self.__name = name 
        self.__donations = []
        if initial_donation is not None:
            self.__donations.append(initial_donation)

    def __str__(self):
        return "[Donor name={}, donations={}]".format(self.__name, self.__donations)
    
    def add_donations(self, donation):
        self.__donations.append(donation)

    @property
    def name(self):
        return self.__name
    
    @property
    def donations(self):
        return self.__donations
    
    @property
    def num_donations(self):
        return len(self.__donations)
    @property
    def total_donations(self):
        return sum(self.__donations)
    
    @property
    def avg_donations(self):
        return self.total_donations / self.num_donations

    def generate_report_row(self):
        return '{:20} ${:>14.2f}{:>16d} ${:>13.2f}'.format(self.name, self.total_donations, self.num_donations, self.avg_donations)

    def __eq__(self, other):
        return self.total_donations == other.total_donations

    def __lt__(self, other):
        return self.total_donations < other.total_donations


class DonorCollection:
    def __init__(self):
        self.__donors = {} # name: donor pairs

    def add_new_donor(self, name):
        if name in self.__donors:
            raise ValueError('name ({}) already exists'.format(name))
        self.__donors[name] = Donor(name)

    def add_donation(self, donor, donation):
        return self.__donors[donor].add_donations(donation)

    def get_donor(self, donor):
        return self.__donors[donor]
    
    def get_donor_names(self):
        return self.__donors.keys()
    
    def get_donors(self):
        return self.__donors.values()

    def generate_report(self):
        '''format and generate a donation report based on current donor collection'''
        header = '{:20}|{:>15}|{:>15}|{:>14}'.format("Donor Name",'Total Given', 'Num Gifts', 'Average Gift')
        line = "-"*67
        lines = [header,line]

        for donor in self.sort_donors():
            lines.append(donor.generate_report_row())
        return '\n'.join(lines)

    def sort_donors(self):
        '''sort donor objects based on it's total donation'''
        return sorted(self.__donors.values(), reverse=True)

    def send_letters_to_all(self):
        for name in self.__donors:
            try:
                with open(self.get_file_name(os.getcwd(), name), "w") as file:
                    file.write(self.get_a_thank_you_letter(name, self.__donors[name].donations[-1]))
            except FileNotFoundError as fnf_error:
                print(fnf_error)

    def get_file_name(self, path, file_name):
        '''normalize a file name for a given donor name'''
        # replace whitespace , * < > / \ ? % : | " . with underscore _
        file_name = re.sub(r'[\s+|,|*|<|>|/|\\|?|%|:|\||"|.]', '_', file_name)
        if not os.path.exists(path):
            os.mkdir(path)
        return os.path.join(path, f'{file_name}.txt')

    def get_a_thank_you_letter(self, name, amount):
        letter = f'Dear {name},\n\n\tThank you for your generous donation of ${amount}.\n\n\tYour kindness is really making the world different!\n\n\t\tSincerely,\n\t\tMailroom Bot'
        return letter