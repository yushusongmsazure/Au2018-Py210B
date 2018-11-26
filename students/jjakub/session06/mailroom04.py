#!/usr/bin/env python3
import sys
import tempfile

"""
Class: Python 210 B, Au2018
Exercise: Session 06, Mailroom Part 04
Student: Jason Jakubiak
"""

user_options = {
    "Send": "Send a Thank You to a single donor",
    "Report": "Create a Report",
    "Letter": "Send a letter to all donors",
    "Quit": "Quit",
    }

donor_db = {
    "jeff": [183.00, 200.00],
    "alex": [53898.23, 2653.00, 105.07],
    "paul": [33941.98],
    "mark": [1.65, 55.00],
    "john": [2705.71],
    }

thanks_txt = (
    "\nDear {},"
    "\nThank you for the donation of ${:.2f}."
    "\nSincerely,"
    "\nThe Mailroom Foundation\n"
    )

col_nm = ("Donor Name |", 
    "Total Given |",
    "Num Gifts |",
    "Average Gift |",
    )

row_sep = ('-' * sum([len(i) for i in col_nm]))

saved_txt = "Letters were successfully saved to "

menu_txt = ("\n Would you like to:"
    "\n 1 - {Send}"
    "\n 2 - {Report}"
    "\n 3 - {Letter}"
    "\n 4 - {Quit}"
    "\n >>> ")


def sort_key(sort):
    return sort[1]


def input_name():
    donor_nm = input("Please enter the full name: ").lower()
    return donor_nm


def input_amt():
    while True:
        try:
            donor_amt = int(input("Please enter the donation amount: "))
            return donor_amt
        except ValueError:
            print("Warning: Please enter an integer!")


def create_msg(name, amt):
    msg = (thanks_txt.format(name.capitalize(), amt))
    return msg


def donor_list():
    for donor, amt in donor_db.items():
        print("{}".format(donor).capitalize())


def send_thanks():
    name = input_name()
    if name == "list":
        donor_list()
    else:
        amt = input_amt()
        donor_db.setdefault(name,[]).append(amt)
        print(create_msg(name, amt))


def donor_calc(donor_db):
    donor_sum = [
            (donor.capitalize(), sum(amt), len(amt), sum(amt)/len(amt)) 
            for donor, amt in donor_db.items()
            ]
    return donor_sort(donor_sum)


def donor_sort(donor_seq):
    donor_sort = sorted(donor_seq, key=sort_key, reverse=True)
    return donor_sort


def donor_rpt():
    print("{:13}{:<11}{:<11}{:<11}".format(*col_nm) + "\n" + row_sep)
    for donor, amt, len, avg in donor_calc(donor_db):
        print("{:13} ${:>11.2f}{:>11} ${:>11.2f}".format(donor, amt, len, avg))


def input_path():
    path = input("Please enter the path: ")
    if not path == "":
        path = path + "\\"
    return path


def write_letter(letter_path):
    for donor, amt, len, avg in donor_calc(donor_db):
        with open("{}{}.txt".format(letter_path, donor), "w") as thank_you:
            thank_you.write(create_msg(donor, amt))


def print_thanks(thx_pth):
    if thx_pth != "":
        print(saved_txt + "{}".format(thx_pth).replace("\\",""))
    else:
        print(saved_txt + "the current directory.")


def thanks_all():
    while True:
        try:
            thanks_path = input_path()
            write_letter(thanks_path)
            print_thanks(thanks_path)
            return
        except FileNotFoundError:
            print("Warning: Please enter a valid path!\n")


def exit_program():
    print("Bye!")
    sys.exit()


switch_dict = {
    1: send_thanks,
    2: donor_rpt,
    3: thanks_all,
    4: exit_program,
    }

def menu():
    main_menu = (menu_txt.format(**user_options))
    return main_menu


def input_main():
    response = int(input(menu()))
    return response


def main():
    while True:
        try:
            switch_dict.get(input_main())()
        except TypeError:
            print("Warning: Please enter an valid option!")
        except ValueError:
            print("Warning: Please enter an valid integer!")

if __name__ == "__main__":
    main()