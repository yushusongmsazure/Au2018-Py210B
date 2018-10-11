import random
import datetime

names = '''
Arasim  David
Chen    Qi
Cheung  Jackie
Degraw  Shawn D
Guo Ying
Jakubiak    Jason
Meese   Tim
Minavi  Alexander
Morrison    Isaac
Nalla   Arun K
Nguyen  Brandon Q
Schirra Rachel Elizabeth
Song    Yushu
Tetteh  Laud N
'''

names = [name for name in names.split('\n') if name] #if name [!= name] ??
random.shuffle(names)

date = datetime.date(2018, 10, 3)

print("Here's the order of Authum 2018 PYTHON210B lightening talks! (two students every week):")
print()
for i, name in enumerate(names, 1): #eumerate gives index number for each value in list
    if i % 2 == 1: # % is modular arguement, in this case testing if i is odd number
        date += datetime.timedelta(days=7)
    if date == datetime.date(2018, 11, 21): # Thanksgiving 2018
        date += datetime.timedelta(days=7)
    name_parts = name.split('\t')
    print('{:2}. ({}) {} {}'.format(i, date, name_parts[1], name_parts[0]))