#!/usr/bin/env python3

"""session09, assignment oo mailroom, Rachel Schirra"""

import datetime

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
        output = ("Dear {name},\nThank you for your recent donation in the "
            "amount of ${amount:.2f}.\n ").format(name=self.name.title(),
            amount=self.donations[-1])

        if self.count_donations > 1:
            output += ("You have donated {count} times for a total of "
                "${total:.2f}! ").format(count=self.count_donations,
                total=self.total_donations)
        else:
            output += ("We greatly appreciate your generous contribution to "
                "our cause! ")

        output += ("We will ensure that these funds are put to good use "
            "defending the universe.\nSincerely,\nThe Bravest Warriors")
        
        return output
    
    def generate_report_row(self):
        output = "{name:20} | ${total:>12.2f} | {count:>12} | ${avg:>12.2f}"
        return output.format(name=self.name.title(), 
            total=self.total_donations, 
            count=self.count_donations, 
            avg=self.avg_donation)


class DonorCollection():
    def __init__(self):
        self.__donors = {} # name: Donor pairs
    
    def add_new_donor(self, name, donation=None):
        if name in self.__donors:
            raise ValueError('Name ({}) already exists.'.format(name))
        self.__donors[name] = Donor(name)
        if donation:
            self.__donors[name].add_donation(donation)
    
    def get_donor(self, name):
        return self.__donors[name]

    def generate_report(self):
        output = '\n\n{:<21}| {:>13} |{:>13} |{:>14}'.format("Donor Name",
            "Total Given", 
            "Num Gifts", 
            "Avg Gift")
        for name in self.__donors.keys():
            output += self.get_donor(name).generate_report_row()
            output += ("---------------------|---------------|--------------"
                "|--------------")

    def generate_all_letters(self, folder):
        dest = "{user_dir}/{date}_{name}.txt"
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        for name in self.__donors.keys():
            d = self.get_donor(name)
            path = dest.format(user_dir=folder, name=name, date=date)
            with open(path, "w") as f:
                f.write(d.generate_letter())
    
    
if __name__ == '__main__':
    dc = DonorCollection()