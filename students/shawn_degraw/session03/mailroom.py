#Mailroom Part 1
import sys

donor_db = [("John Smith", [500.00, 150.00, 20.00]),
            ("Jane Doe", [340.00, 30.00, 200.00]),
            ("Jason Bourne", [240.00, 140.00]),
            ("John Wick", [1000.00]),
            ("GI Jane", [150.00, 60.00])
           ]

thankyouletter = "\n".join(("","Dear {name},","","Thank you for your generous donation of ${amount:.2f} to our cause.","Your donations help keep Python great!","","Sincerely","","The Python Project",""))

def printthankyou(donoridx):
    print(thankyouletter.format(name=donor_db[donoridx][0], amount=donor_db[donoridx][1][len(donor_db[donoridx][1])-1]))

def adddonation(donoridx):
    donationammount = input("Enter donation amount> ")
    donor_db[donoridx][1].append(float(donationammount))

def printdonorlist():
    for name in donor_db:
        print(name[0])

def handlename(namechoice):
    #getting the name index starting from 1 to use truthiness in if statement
    nameidx = [idx for idx, nametuple in enumerate(donor_db,1) if nametuple[0] == namechoice]
    if nameidx:
        print("Using this person: {}".format(donor_db[nameidx[0]-1]))
        adddonation(nameidx[0]-1)
        printthankyou(nameidx[0]-1)
    else:
        print("Adding name to DB.")
        donor_db.append((namechoice, []))
        adddonation(len(donor_db)-1)
        printthankyou(len(donor_db)-1)

def exit_program():
    print("Thank you. Bye")
    print(donor_db)
    sys.exit()

def main():
    """Mailroom main program loop with menu"""

    menu = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

    while True:
        choice = input(menu)
        if choice == '1':
            name = input("Please enter full name> ")
            if name == "list":
                printdonorlist()
            else:
                handlename(name)
        elif choice == '2':
            print("Selected 21")
        elif choice == '3':
            exit_program()
        else:
            print("bad choice")

if __name__ == "__main__":
    main()
