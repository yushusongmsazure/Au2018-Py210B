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
from donor_models import *
  
dc = DonorCollection()

prompt = "\n".join(("Welcome to mailroom bot!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - quit",
          ">>> "))

def init(dc):
    '''initialize donor db'''
    dc.add_new_donor("William Gates, III")
    dc.add_donation("William Gates, III", 653772.32)
    dc.add_donation("William Gates, III", 12.17)

    dc.add_new_donor("Jeff Bezos")
    dc.add_donation("Jeff Bezos", 877.33)

    dc.add_new_donor("Paul Allen")
    dc.add_donation("Paul Allen", 663.23)
    dc.add_donation("Paul Allen", 43.87)
    dc.add_donation("Paul Allen", 1.23)

    dc.add_new_donor("Mark Zuckerberg")
    dc.add_donation("Mark Zuckerberg", 1663.23)
    dc.add_donation("Mark Zuckerberg", 4300.87)
    dc.add_donation("Mark Zuckerberg", 10432.0)

    dc.add_new_donor("Elon Musk")
    dc.add_donation("Elon Musk", 250000)
    dc.add_donation("Elon Musk", 15000)

def send_a_thank_you():
    '''send a thank you letter to a donor after each donation'''
    while True:
        name = input("Who do you want to send this to, use a full name: ")
        if name.lower() == 'list':
            print("\n".join(dc.get_donor_names()))
        else:
            break

    while True:
        try:
            amount = float(input("How much do you want to donate? "))
            if name not in dc.get_donor_names():
                dc.add_new_donor(name)

            dc.add_donation(name, amount)
            print(dc.get_a_thank_you_letter(name, amount))
        except ValueError:
            print("Please enter a valid donation!")
        else:
            break

def send_letters_to_all():
    '''Write to a file for each donor of their last donation'''
    return dc.send_letters_to_all()

def create_a_report():
    print(dc.generate_report())

def exit_program():
    print("Bye!")
    sys.exit()

choice_dict = {"1":send_a_thank_you,
               "2":create_a_report,
               "3":send_letters_to_all,
               "4":exit_program}

def main():
    init(dc)
    while True:
        try:
            response = input(prompt)
            choice_dict[response.strip()]()
        except Exception as ex:
            print(f"You got an error {ex}. Please choose 1-4!")

if __name__ == "__main__":
    main()