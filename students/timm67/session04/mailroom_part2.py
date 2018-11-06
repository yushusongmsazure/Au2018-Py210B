#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Mailroom Part 2 assignment
"""

import collections
from collections import defaultdict

# Revised donor database uses tuples for names instead of a single string

donors = { 
     ('Jim', 'Tillson')   : [5.00, 20.00],
     ('Barb', 'Langley')  : [10.00, 20.00, 100.00],
     ('Jen',  'Garfield') : [10.00, 20.00, 5.00],
     ('Rex',  'Miller')   : [20.00, 20.00, 5.00],
     ('Tony', 'Blake')    : [20.00, 20.00, 10.00] 
     }


def send_thankyou_single_donor_task():
    global donors
    donor_found = False
    donor_fname = input("Enter donor first name ('list' for all donors) : ")
    if (donor_fname == 'list'):
        for name in donors.keys():
            print("{}, {} ".format(name[0], name[1]))
        donor_fname = input("Enter donor first name : ")
    donor_lname = input("Enter donor last name : ")
    donor_amt = input("Enter donation value: ")
    try:
        donor_amt = float(donor_amt)
    except ValueError:
        print("Please enter a numeric donation value")
        return
    
    for donor in donors.keys():
        if donor[0] == donor_fname and donor[1] == donor_lname:
            print("{0}, {1} FOUND in dictionary".format(donor_fname, donor_lname))
            donor_found = True
            break

    if donor_found == True:
        # Add the donor's donation
        donors[(donor_fname, donor_lname)].append(donor_amt)
    else:
        print("{0}, {1} NOT found in dictionary, creating...".format(donor_fname, donor_lname))
        donors[(donor_fname, donor_lname)] = [donor_amt]
        donor = (donor_fname, donor_lname)

    fmtline0 = "\n\nDear {0},\n\n"
    fmtline1 = "Many thanks for your recent donation of {0:6.2f}.\n\nWith this donation, your cumulative total of donations is {1:6.2f} with an average donation of {2:6.2f}\n\n"
    fmtline2 = "Thanks again for your generous donation.\n\nBest Regards,\nThe Staff"
    donations = donors[(donor[0], donor[1])]
    total_donations=sum(donations)
    avg_donation = total_donations / len(donations)
    print(fmtline0.format(donor[0]))
    print(fmtline1.format(donations[(len(donations) - 1)], total_donations, avg_donation))
    print(fmtline2)    

def send_thankyou_multiple_donors_task():
    global donors
    file_fmtline0 = "\n\nDear {0},\n\n"
    file_fmtline1 = "Many thanks for your recent donation of {0:6.2f}.\n\nWith this donation, your cumulative total of donations is {1:6.2f} with an average donation of {2:6.2f}\n\n"
    file_fmtline2 = "Thanks again for your generous donation.\n\nBest Regards,\nThe Staff"
    for donor in donors.keys():
        filename = "./{0}_{1}.txt".format(donor[0], donor[1])
        print("Writing {0}...".format(filename))
        donations = donors[(donor[0], donor[1])]
        total_donations=sum(donations)
        avg_donation = total_donations / len(donations)
        with open(filename, 'w') as handle:
            handle.write(file_fmtline0.format(donor[0]))
            handle.write(file_fmtline1.format(donations[(len(donations) - 1)], total_donations, avg_donation))
            handle.write(file_fmtline2)

def formatter(fname, lname, in_list):
    list_len = len(in_list)
    fmt_string = "{0:15} {1:15} ".format(fname, lname)
    fmt_string += list_len * '{:6.2f}, '
    return fmt_string.format(*in_list)

def create_report_task():
    global donors
    report_fmt_str_hdr = "{0:15} {1:15} {2:10}"
    print(report_fmt_str_hdr.format('First Name', 'Last Name', ' Donations'))
    for key in donors.keys():
        print(formatter(key[0], key[1], donors[key]))

def print_menu():
    print("Mailroom Tasks")
    print("[1] Send a Thank you to a single donor")
    print("[2] Create a report")
    print("[3] Send letters to all donors")
    print("[9] Exit Mailroom")
    pass

def main():
    exitMail = False
    while(exitMail == False):
        print_menu()
        response = input("Enter Mailroom Option: ")
        try:
            response = int(response)
        except(ValueError):
	        print("Enter a number between 1-9")
	        continue
        if (response == 9):
            exitMail = True
        elif (response == 3):
            send_thankyou_multiple_donors_task()
            pass
        elif (response == 2):
            create_report_task()
            pass
        elif (response == 1):
            send_thankyou_single_donor_task()
            pass
        else:
            print("Invalid response entered\n")

if __name__ == "__main__":
    main()
