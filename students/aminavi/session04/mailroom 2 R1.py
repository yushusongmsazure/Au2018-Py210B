import sys

thank_you_action = "Send a Thank You to a single donor."
create_a_report = "Create a Report"
thank_you_action_all = "Send letters to all donors."
quit_action = "quit"

donor_list = {
    'william': [653772.32 , 953772.32,100000],
    'jeff': [8888777.22 ,877.33],
    'paul': [663.23, 43.87 ,1.32],
    'mark': [1663.23, 4300.87, 10432.00],
    'nigel': [5000000 , 10]
    }
def sort_key(donor_list):
    return sum(donor_list.values())

def send_thank_you():
    name = ''
    while not name or name.lower() == 'list':
        name = input("Please enter the full name: ")
        if name.lower() == 'list':
            donor_list.setdefault(name.lower(),[])
    donation = int(input("Please enter the donation amount: "))
    for i in range(len(donor_list.keys())):
        if name.lower() in  donor_list.keys():
            donor_list[name.lower()].append(donation)
        donor_list.setdefault(name.lower(),[donation])
        break


def create_report():
    print('\n\n')
    print('{:<25}|{:^17}|{:^15}|{:^17}'.format('Donor Name','Total Given','Num Gifts', 'Average Gift'))
    print(75 * '-')
    sorted(donor_list, key=sort_key, reverse=True)
    for key, value in donor_list.items():
        print(f'{key:25}', f'${sum(value):>17.2f}', f'{len(value):^15}', f'${(sum(value)/len(value)):>17.2f}')

# def thank_you_action_all():

def Main():
    prompt = ("Select an action: \n1.{}\n2.{}\n3.{}\n4.{}\n".format(thank_you_action, create_a_report, thank_you_action_all, quit_action))
    while True:
        response = input(prompt)  # continuously collect user selection
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            thank_you_action_all()
        elif response == "4":
            print('Bye')
            sys.exit()
        else:
            print("Not a valid option!")


if __name__ == '__main__':
   Main()