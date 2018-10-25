#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Mailroom assignment
"""

import collections
from collections import defaultdict

def print_menu():
    print("Mailroom Tasks")
    print("[1] Send Thank you")
    print("[2] Create report")
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
            pass
        elif (response == 1):
            pass
        else:
            print("Invalid response entered\n")

if __name__ == "__main__":
    main()
