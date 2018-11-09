#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Mailroom Part 2 assignment
"""

import collections
from collections import defaultdict

#
# Revised donors database is an array of dictionaries with appropriate keynames. 
# 'amounts' remains a list of donation values 
# 

donors = [
    { 'fname' : 'Jim',  'lname' : 'Tillson',  'amounts' : [5.00, 20.00]},
    { 'fname' : 'Barb', 'lname' : 'Langley',  'amounts' : [10.00, 20.00, 100.00]},
    { 'fname' : 'Jen',  'lname' : 'Garfield', 'amounts' : [10.00, 20.00, 5.00]},
    { 'fname' : 'Rex',  'lname' : 'Miller',   'amounts' : [20.00, 20.00, 5.00]},
    { 'fname' : 'Tony', 'lname' : 'Blake',    'amounts' : [20.00, 20.00, 10.00]},
]

def send_thankyou_task():
    donor_found = False
    donor_name = input("Enter donor name ('list' for all donors) : ")
    if (donor_name == 'list'):
        for donor in donors:
            print("{}, {} ",donor['lname'], donor['fname'])
        donor_fname = input("Enter donor first name : ")
        donor_lname = input("Enter donor last  name : ")
    donor_amt = input("Enter donation value: ")
    try:
        donor_amt = float(donor_amt)
    except ValueError:
        print("Please enter a numeric value")
        return
    
    for donor in donors:
        if donor['fname'] == donor_fname and donor['lname'] == donor_lname:
            print("{0}, {1} FOUND in dictionary".format(donor_lname, donor_fname))
            donor['amounts'].append(donor_amt)
            donor_found = True
            break

    # if we got to here, donor is not in dictionary, so create a new donor
    if donor_found == False:
        print("{0}, {1} NOT found in dictionary, creating...".format(donor_lname, donor_fname))
        new_donor = { 'fname' : str(donor_fname), 'lname' : str(donor_lname), [].append(donor_amt) }
        donors.append(new_donor)

    a = 0.0
    donations = donors[donor_name]
    for x in donations:
        a += x
    fmtline0 = "\n\nDear {0},\n"
    fmtline1 = "Many thanks for your recent donation of {0:6.2f}. With this donation, your cumulative total is {1:6.2f}\n"
    fmtline2 = "Thanks for your donation. \n\n"
    print(fmtline0.format(donor_name))
    print(fmtline1.format(donor_amt, a))
    print(fmtline2)
    pass

def create_report_task():
    for d in donors:
        print("{}\t".format(d))
        avg = 0.0
        donations = donors[d]
        for x in donations:
            print("{:6.2f}\t".format(x))
            avg += x
        numd = len(donations)
        avg = avg / numd
        print("{:6.2f}\t{}\n".format(avg, numd))
    pass

def print_menu():
    print("Mailroom Tasks")
    print("[1] Send a Thank you")
    print("[2] Create a report")
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
        elif (response == 5):
            pass
        elif (response == 4):
            pass
        elif (response == 3):
            pass
        elif (response == 2):
            create_report_task()            
            pass
        elif (response == 1):
            send_thankyou_task()
            pass
        else:
            print("Invalid response entered\n")

if __name__ == "__main__":
    main()
