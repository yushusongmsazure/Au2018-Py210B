#!/usr/bin/python

##################################################
## Author: Jackie Cheung
## Date: 2018/10/23
## Version: 0.1
## Class: Au2018-Py210B
## Description: Mailroom Part 1 - sending Thank You email and create report
##################################################

import sys  # imports go at the top of the file

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ]

prompt = "\n".join(("Welcome to the Mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))


def get_donor():
    donor_list = []
    for item in donor_db:
        donor_list.append(item[0])
    return donor_list


def send_a_thank_you():
    name = input("Please enter the full name of the donor: ")
    donor_list = get_donor()
    if name == "list":
        print("\n".join(donor_list))
        print()
    elif name in donor_list:
        print("Adding donation to existing donor")
        print("Before adding donation:\n", donor_db)
        amount = float(input("Please enter the amount of donation: "))
        for donor in donor_db:
            if name == donor[0]:
                donor[1].append(amount)
        print("After adding donation:\n", donor_db)
        send_email(name, amount)
    else:
        print("Adding new donor entry to the db")
        print("Before adding new donor entry:\n", donor_db)
        amount = float(input("Please enter the amount of donation: "))
        new_donor_entry = (name, [amount])
        donor_db.append(new_donor_entry)
        print("After adding new donor entry:\n", donor_db)
        send_email(name, amount)


# Sending a nicely formatted Thank you email
def send_email(name, amount):
    print('\n---------- Sending Thank You email ----------\n')
    print('Dear {},'.format(name))
    print('\nThank you very much for your generous donation of ${:,}.'.format(amount))
    print('\nYour generous help is very appreciated. Have a wonderful day!')
    print('\nYour Sincerely,')
    print('The Mailroom')
    print('\n----------    End of the email     ----------\n')


# Creating a donation history report
def create_a_report():
    print('{:23} | {:10} | {:8} | {:10}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('----------------------------------------------------------------')
    for i, item in enumerate(donor_db):
        print('{:24} ${:12.2f}{:12} ${:12.2f}'.format(donor_db[i][0], sum(donor_db[i][1]), len(donor_db[i][1]), sum(donor_db[i][1])/len(donor_db[i][1])))
    print()


# Exiting the program
def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_a_thank_you()
        elif response == "2":
            create_a_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()