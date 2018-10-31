import sys

thank_you_action = "Send a Thank You to a single donor."
create_a_report = "Create a Report"
thank_you_action_all = "Send letters to all donors."
quit_action = "quit"

donor_list = {
    'William': [653772.32 , 953772.32,100000],
    'Jeff': [8888777.22 ,877.33],
    'Paul': [663.23, 43.87 ,1.32],
    'Mark': [1663.23, 4300.87, 10432.00],
    'Nigel': [5000000 , 10]
    }

# def send_thank_you():
#     name = ''
#     while not name or name.lower() == 'list':
#         name = input("Please enter the full name: ")
#         if name.lower() == 'list':
#             print(' '.join(x[0] for x in donor_list))
#     donation = int(input("Please enter the donation amount: "))
#     for i in range(len(donor_list)):
#         if name.lower() in donor_list.lower():
#             donor_list[i][1].append(donation)
#             return
#     donor_list.append((name, [donation]))

def create_report():
    print('\n\n')
    print('{:<25}|{:^17}|{:^15}|{:^17}'.format('Donor Name','Total Given','Num Gifts', 'Average Gift'))
    print(75 * '-')
    for key, value in donor_list.items():
        print(f'{key:25}', f'${sum(value):>17.2f}', f'{len(value):^15}', f'${(sum(value)/len(value)):>17.2f}')


if __name__ == '__main__':
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