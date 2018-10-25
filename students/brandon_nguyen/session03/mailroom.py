import sys
import unittest
from decimal import Decimal

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
   #elif response.strip() in donor_db:
    else:
        print(response.strip())
        for name in donor_db:
            #print(name[0])
            if name[0] == response.strip():
                indx = donor_db.index(name)
                donation = float(input("Please enter donation amount for " + name[0] + ": "))
                donor_db[indx][1].append(donation)
                print("\n\nHello {},\nThank you so much for the generious donation of {}!\n\n".format(name[0],float(donation)))
                break
        else:
            donor_db.append((response.strip(),[0])) #adding new name with $0 donation.
    #print(donor_db)       

        

def sort_seq(seq):
    pass

def create_rpt():
    newList = sort_sum()
    header_string = "Donor Name               | Total Given | Num Gifts | Average Gift"
    line = '-'*len(header_string)
    print(header_string)
    print(line)
    for donor, total, num, avg in newList:
        print(donor, "\t\t", "$  ",total[0], "\t    ",num[0], "\t\t$  {0:.2f}".format(avg[0])   )



def sort_sum():
    #creating a new list with computed value for easy printing.
    """
    This function returned a sorted list of by on order amount3
    """
    dbSum = []
    for name, donation in donor_db:
        dbSum.append((name,[sum(donation)],[len(donation)],[sum(donation)/len(donation)]),)
    return sorted(dbSum, key=lambda donor: donor[1], reverse=True)
    

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