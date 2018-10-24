#!usr/bin/en python
donors_list = [('Aron 123', [10,5]), ('Becky', [3,30]), ('Charlie',[10,26]),('Thomas',[22,9,4,5]),('Nancy',[1,2,3])]
donors_name = [x for x,y in donors_list]
donors_number = {x: len(y) for x,y in donors_list}
donors_total = {x:sum(y) for x,y in donors_list}

def thank_you(seq):
    name_input = input("Enter a name from the list: ").title()
    if name_input in donors_name:
        print("\nDear Mr.{},\nThank you for donation of ${:.2f} for XYZ Charity Organisation. Its a kind initiative from"
        " you for a nobel cause.\n\nWith Regards\n\nXYZ\n".format(name_input, donors_total[name_input]))
    else:
        print ('Name entered is not in the donor list')
        thank_you(seq)
def donors_thanks(seq):
    name_input = input("Enter the donor of your interest: ").title()
    if name_input == 'List':
        print (donors_name)
        thank_you(seq)
    elif name_input in donors_name:
        print("Dear Mr.{},\nThank you for donation of ${:.2f} for XYZ Charity Organisation. Its a kind intiative from"
        " you for a nobel cause.\n\nWith Regards\n\nXYZ\n".format(name_input, donors_total[name_input]))
    elif name_input !=seq:
        seq.append(name_input)
        print("Dear {},\nI am writing regarding the charity program 'XYZ' for 'ABC' cause. \nIf you are interested"
              " please reply back. Your help will be appreciated.\n\nThank you\nXYZ\n".format(name_input))

def sort_key(sorting):
    return sorting[1]
def create_report(seq):
    list_sort = [(x,sum(y)) for x,y in donors_list]
    list_sorting = (sorted(list_sort,key=sort_key, reverse = True))
    print ("\nList of donors and thier contribution to XYZ Charity\n")
    print ("{:<10}\t\t{:<10}\t\t{:<10}\t\t{:<10}".format('Donors-name','Total','Num gifts', 'Average gift'))
    print ('_ '*30)
    for a,b in list_sorting:
        print ("{:<10}\t\t$ {:<10.2f}\t\t{:<10}\t\t$ {:<10.2f}".format(a,b, donors_number[a], b/donors_number[a]))
    print('_ ' * 30)
    print ('End of Report\n')

def quit_program(seq):
    print ('Thank for using this script.\nHave a nice day\nBye\n')
def main(seq):
    while True:
        response = input("MAIN MENU\nDonors and donations made to XYZ organisation.\nPlease select one "
                         "of the option below to proceed.\n1.Send a Thank you message to the donor\n2. Create a report\n3. Quit\n>>>")  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            donors_thanks(seq)

        elif response == "2":
            create_report(seq)

        elif response == "3":
            quit_program(seq)
            break
        else:
            print("Not a valid option!")
#main(donors_list)
if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main(donors_list)