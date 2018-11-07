#!/usr/bin/env python3

##################################################
## Author: Jackie Cheung
## Date: 2018/10/30
## Version: 0.1
## Class: Au2018-Py210B
## Description: Mailroom Part 2 - Incorporate file writing and dictionary use
##################################################

import sys  # imports go at the top of the file

donor_dict = {("William", "Gates", "III"): [653772.32, 12.17],
              ("Mark", "Zuckerberg"): [1663.23, 4300.87, 10432.0],
              ("Jeff", "Bezos"): [877.33],
              ("Paul", "Allen"): [663.23, 43.87, 1.32]
             }

main_prompt = "\n".join(("Welcome to the Mailroom!",
              "Choose an action:",
              "1 - Send a Thank You to a single donor",
              "2 - Create a Report",
              "3 - Send letters to all donors",
              "4 - Quit",
              ">>> "))


def menu_selection(prompt, dispatch_dict):
    while True: # loop forever until they quit.
        response = input(prompt)
        if dispatch_dict[response]() == "exit program":
            break


def send_a_thank_you():
    name = input("Please enter the full name of the donor: ")
    if name == "list":
        for key in donor_dict.keys():
            print(" ".join(key))
        print()
    elif tuple(name.split()) in donor_dict.keys():
        print("Adding donation to existing donor")
        print("Before adding donation:\n", donor_dict)
        amount = float(input("Please enter the amount of donation: "))
        donor_dict[tuple(name.split())].append(amount)
        print("After adding donation:\n", donor_dict)
        print(send_email(name, amount))
    else:
        print("Adding new donor entry to the db")
        print("Before adding new donor entry:\n", donor_dict)
        amount = float(input("Please enter the amount of donation: "))
        donor_dict[tuple(name.split())] = [amount]
        print("After adding new donor entry:\n", donor_dict)
        print(send_email(name, amount))


# Creating a nicely formatted Thank you email as String
def send_email(name, amount):
    email = ('Dear {},'.format(name) + 
             '\n\n\tThank you for your very kind donation of ${:,}.'.format(amount) + 
             '\n\n\tIt will be put to very good use.'
             '\n\n\t\tSincerely,'
             '\n\t\t   -The Mailroom'
            )
    return email


# Creating a donation history report
def create_a_report():
    print('{:23} | {:10} | {:8} | {:10}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('----------------------------------------------------------------')
    for key, value in donor_dict.items():
        print('{:24} ${:12.2f}{:12} ${:12.2f}'.format(' '.join(key), sum(value), len(value), sum(value)/len(value)))
    print()


# Creating a text letter file for all donors
def send_letters_to_all():
    print("Creating text file letter for all donors")
    for key, value in donor_dict.items():
        filename = '_'.join(key) + '.txt'
        print(filename)
        with open(filename, 'w') as f:
            f.write(send_email(' '.join(key), sum(value)))


# Exiting the program
def exit_program():
    print("Bye! Have a wonderful day!")
    sys.exit()  # exit the interactive script
    return "exit program"


# Main menu selection
main_dispatch = {"1": send_a_thank_you,
                 "2": create_a_report,
                 "3": send_letters_to_all,
                 "4": exit_program,
                 }


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)