#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Mailroom assignment
"""

import collections
from collections import defaultdict

#
# donors dictionary has a key equal to the donor's name and value is an array of donations
#

donors = {
    'Jim Tillson'  : [5.00, 20.00],
    'Barb Langley' : [10.00, 20.00, 100.00],
    'Jen Garfield' : [10.00, 20.00, 5.00],
    'Rex Miller'   : [20.00, 20.00, 5.00],
    'Tony Blake'   : [20.00, 20.00, 10.00]
}

def send_thankyou_task():
    donor_name = input("Enter donor name ('list' for all donors) : ")
    if (donor_name == 'list'):
        for name in donors.keys():
            print(name)
        donor_name = input("Enter donor name : ")
    donor_amt = input("Enter donation value: ")
    try:
        donor_amt = float(donor_amt)
    except ValueError:
        print("Please enter a numeric value")
        return
    if donor_name in donors.keys():
        print("{0} found in dictionary".format(donor_name))
        # add to donations for existing donor (key)
        donors[donor_name].append(donor_amt)
    else:
        # create a new donor (key)
        print("{0} NOT found in dictionary, creating...".format(donor_name))
        donors[donor_name] = [donor_amt]
    print(donors[donor_name])
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
