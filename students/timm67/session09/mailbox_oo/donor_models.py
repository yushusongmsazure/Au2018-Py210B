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

    def generate_report_row(self):
        return '{20!s}|{:>10d}|{:>15f}|{:>15f}'.format(self._name, self.num_donations, self.total_donations, self.avg_donation)
        # TODO: print the report row for this particular donor

#
# Properties
#

    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations

    @property
    def num_donations(self):
        return len(self._donations)

    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def avg_donation(self):
        return float(self.total_donations / self.num_donations)


class DonorCollection:
    def __init__(self):
        # dictionary with name as key and donor object as value
        self._donors = {} 

    def add_new_donor(self, name):
        if name in self._donors:
            raise ValueError('name [{}] already exists'.format(name))
        self._donors[name] = Donor(name)

    def add_donation(self, name, donation):
        try:
            self._donors[name].add_donation(donation)
        except KeyError:
            print('name [{}] not present in collection'.format(name))

    def get_donor(self, name):
        try:
            donor = self._donors[name]
        except KeyError:
            print('name [{}] not present in collection'.format(name))
        return donor

    def generate_report(self):
        header = '{20!s}|{:>10s}|{:>15s}|{:>15s}'.format('Name', 'Num Donations', 'Total Donations', 'Avg Donation')
        lines = [header]
        for donor in self._donors.values():
            lines.append(donor.generate_report_row())
        return '/n'.join(lines)

    def save_letters_to_file(self):
        pass


if __name__ == '__main__':
    dc = DonorCollection()
    dc.add_new_donor('Bill')
    dc.add_donation('Bill', 1234)
    dc.add_donation('Bill', 5678)
    dc.add_new_donor('Paul')
    dc.add_donation('Paul', 1234)
    dc.add_donation('Paul', 5678)




    


