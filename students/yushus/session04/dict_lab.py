
# dict_lab = {"Bill":[12,13,14],
#             "Paul":[1827,90]}
# sorted_dict={}
# sorted_name = sorted(dict_lab,key=lambda t: sum(dict_lab[t]), reverse=True)

# for name in sorted_name:
#     sorted_dict[name]=[sum(dict_lab[name]), len(dict_lab[name]), sum(dict_lab[name])/len(dict_lab[name])]

# for i in sorted_dict:
#     print()

# with open('yushus.txt', 'w') as f:
#     f.writelines("read_data")
# f.closed
# True

# d=dict_lab
# donor_table=[]
# for d in dict_lab:
#     donor_table.append([d, sum(dict_lab[d])])

letter = '''
        Dear {name},
        Thank you for your generous donation of ${amount}. Your kindness is really making the world different!

        Sincerely,
        Mailroom Bot
        '''
print(letter)