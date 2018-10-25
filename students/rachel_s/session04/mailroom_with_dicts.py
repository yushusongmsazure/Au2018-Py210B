#!/usr/bin/env python3

import csv

# Import donor data

donor_info = {}

with open('mailroom/donors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if not line[0].lower() in donor_info:
            donor_info[line[0].lower()] = [int(line[1])]
        else:
            donor_info[line[0].lower()].append(int(line[1]))

csv_file.close

def user_menu():
    menu = {1: send_thank_you, 2: create_report, 3: quit}
    response = input("Select an option:\n  1  Send a thank you\n  2  Create a report\n  3  Quit\n\n> ")
    if int(response) in menu.keys():
        menu.get(int(response))()
    else:
        response = input("Please select 1, 2, or 3.\n> ")

# Send a thank you
def send_thank_you():
    donor_name = input("What is the donor's full name?\n> ").lower()
    if donor_name == 'list':
        for i in donor_info.keys():
            print(i.title())
        user_menu()
    else:
        donation = int(input("Please enter the donation amount.\n> "))
        if donor_name in donor_info:
            donor_info[donor_name].append(donation)
        else:
            donor_info[donor_name] = [donation]
        donation_count = len(donor_info.get(donor_name))
        donation_total = sum(donor_info.get(donor_name))
        thank_you_note = "Dear {name},\nThank you for your recent donation in the amount of ${amount:.2f}. "
        
        if donation_count > 1:
            thank_you_note += "You have donated {count} times for a total of ${total:.2f}! "
        else:
            thank_you_note += "We greatly appreciate your generous contribution to our cause! "
        thank_you_note += "We will ensure that these funds are put to good use defending the universe.\nSincerely,\nThe Bravest Warriors"
        print(thank_you_note.format(name=donor_name.title(), amount=donation, count=donation_count, total=donation_total))
        print(donor_name)
        print(donation_count)
        print(donation_total)


# Create a report
def create_report():
    colnames = ["Donor Name", "Total Given", "Num Gifts", "Avg Gift"]
    title = "{:<21}| {:>13} |{:>13} |{:>14}".format(colnames[0], colnames[1], colnames[2], colnames[3])
    mystr = "{name:20} | ${total:>12.2f} | {count:>12} | ${avg:>12.2f}"
    print(title)
    print("---------------------|---------------|--------------|--------------")
    for name, donations in donor_info.items():
        print(mystr.format(name=name.title(), total=sum(donations), count=len(donations), avg=(sum(donations)/len(donations))))
    user_menu()

if __name__ == "__main__":
    user_menu()