import sys
import unittest

#!/usr/bin/env python3
#Week3 Excercise mailroom part 1
#Student: Brandon Nguyen - Au2018

#global define data structure
donor_db = [("Brandon Nguyen", [4500,350,300.05]),
          ("Shawn DeGraw", [5500, 345,571.3]),
          ("Jacqueline Lee",[4300,3200,230.1]),
          ("Aidan Nguyen", [4300,200,238.2]),
          ]
promptTxt = "\n".join(("Welcome to the mailroom program!",
          "Please choose from below 3 options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))
#The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

#think about a main menu function that can be called any where.
def main_menu():
    promptTxt = "\n".join(("Welcome to the mailroom program!",
          "Please choose from below 3 options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

def send_ty():
    response = input("\nPlease enter donor full names or \"list\": " )
    if response.strip() == 'list':
        list_donors()

def add_donor():
    pass

def fmt_email():
    pass

def get_add_donation():
    pass

def sort_seq(seq):
    pass

def create_rpt():
    pass

def list_donors():
    lst = []
    for name in donor_db:
        lst.append(name[0])
    lst.sort()
    print()
    for name in lst: print(name)
    print()

def quit_program():
    print("Thank you for trying mailroom!")
    sys.exit()  # reason to import sys

def main():
    while True:
        response = input(promptTxt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection   
        if response == "1":
            send_ty()
        elif response == "2":
            create_rpt()
        elif response == "3":
            quit_program()
        else:
            print("\nNot a valid option! Please enter value 1,2 or 3.\n")


if __name__ == '__main__':
    #ask the intend of the comment in class
    main() 