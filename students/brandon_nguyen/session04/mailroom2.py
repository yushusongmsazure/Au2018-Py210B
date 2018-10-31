
#!/usr/bin/env python3
#Week3 Excercise mailroom part 2
#Student: Brandon Nguyen - Au2018
import sys
import unittest
from decimal import Decimal


#global define data structure
#dictionary {peron:[donations]}
donor_db = {"Brandon Nguyen": [4500.33,350.87,300.05],
          "Shawn DeGraw": [5500.00, 345.05,571.33],
          "Jacqueline Lee":[4300.00,3200.00,230.13],
          "Aidan Nguyen" : [4300.00,200.00,238.23],
        }
promptTxt = "\n".join(("\nWelcome to the mailroom program!\n",
          "Please choose an options:\n\n",
          "1 - Send a Thank You to a single donor.",
          "2 - Create a Report.",
          "3 - Send letters to all donors.",
          "q - Quit",
          ">>> "))
#building switch case menu with dictionary


#The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

#think about a main menu function that can be called any where.
def show_menu(promptxt, select_dict):
    while True:
        menu_selected = input(promptTxt)
        if select_dict[menu_selected]() == "Exit Menu":
            break


def send_ty():
    while True:
        response = input("\nPlease enter donor full names or \"list\". Q to return to main menu: " )
        if response.strip() == 'list':
            list_donors()
            break
        elif response.strip() == 'Q':
            return
        else:
            for person in donor_db:
            #print(name[0])
                if person == response.strip():
                    #indx = donor_db.index(name)
                    while True:
                        donation = input("Please enter donation amount for " + name[0] +". Q to quit. :>>")
                        if donation.strip() == 'Q':
                            main()
                        else:
                            break
                    donor_db[indx][1].append(float(donation))
                    print("\n\nHello {},\nThank you so much for the generious donation of {}!\n\n".format(name[0],float(donation)))
                    return
            else:
                #donor_db.update((response.strip(),[0.00])) #adding new name with $0 donation. avoiding div/0 issue
                addNew_person(response.strip(),donor_db)

def send_ty_all():
    pass

def create_rpt():
    """
    This function is to print the report of donor.  
    """
    #Currently need more work on the format as 0.0 problem not yet solved.
    print()
    newList = sort_sum() #creating a new list with sorted total in reverse already for easy printing.
    header_string = "Donor Name              |  Total Given | Num Gifts | Average Gift"
    line = '-'*len(header_string)
    print(header_string)
    print(line)
    for donor, total, num, avg in newList:
        print( donor, "\t\t$ ",str(total[0]).rjust(13), str(num[0]).rjust(5), "\t   $ ", str(avg[0]).rjust(10) )
    print("\n\n")
      
def sort_sum():
    #creating a new list with computed value for easy printing.
    """
    This function returned a sorted list of by on order amount3
    """
    dbSum = []
    for name, donation in donor_db:
        dbSum.append((name,[round(sum(donation),2)],[len(donation)],[round(sum(donation)/len(donation),2)]),)
    return sorted(dbSum, key=lambda donor: donor[1], reverse=True)
    
def list_donors():
    """
    Basic Name of donor return in Order by First Name
    """
    lst = []
    for name in donor_db:
        lst.append(name[0])
    lst.sort()
    print()
    for name in lst: print(name)
    print()
#breaking down to sub function
def addNew_person(newName, db):
    newRcd = {newName:[0.00]}
    db.update(newRcd)

def update_donation(name,newDonation,db):
    cur_donation = db.get(name)
    db[name] = cur_donation.append(newDonation)    


def quit_program():
    print("Thank you for trying mailroom!")
    sys.exit()  # reason to import sys
#a better way to exit
def exit_menu():
    print("\nExiting the menu.")
    return "Exit Menu"


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

#lesson learned - the value as function need to be below the defined function otherwise error - NameError 'send_ty' is not defined.
select_dict = {
                "1": send_ty, 
                "2": create_rpt, 
                "3": send_ty_all, 
                "q": exit_menu
                }

if __name__ == '__main__':
    #ask the intend of the comment in class
    #main()
    show_menu(promptTxt, select_dict) 