

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
        return '|{20!s}|{:>10d}|{:>15f}|{:>15f}'.format(self.name, self.num_donations, self.total_donations, self.avg_donations)

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
    
    def generate_report(self):
        header = '|{20!s}|{:>10d}|{:>15f}|{:>15f}'.format("Name", '# donations', 'Total','AVG')
        lines = [header]
        for donor in self.__donors.values():
            lines.append(donor.generate_report_row())

        return '\n'.join(lines)