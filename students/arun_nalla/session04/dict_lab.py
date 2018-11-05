#!/usr/bin/env python3
"""Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle”
who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)"""
#Dictionary-1
my_dict = {}
my_dict['Name'] = 'Chris'
my_dict['City'] = 'Seattle'
my_dict['Cake'] = 'Chocolate'
print (my_dict)
# Delete the entry for “cake” and Display the dictionary.
my_dict.pop('Cake')
print (my_dict)
# Add an entry for “fruit” with “Mango” and display the dictionary.
my_dict['Fruit'] = 'Mango'
print(my_dict)
# Display the dictionary keys.  Display the dictionary values.
print (my_dict.keys())
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print ('Cake' in my_dict)
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print ('Mango' in my_dict.values())

#Dictionary -2
my_dict_2 = {}
for keys,values in my_dict.items():
    if 't'.upper() or 't'.lower() in values:
        t = values.count('t')
        my_dict_2[keys]=t
print(my_dict_2)


#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
s2 = set([x for x in range(1,21) if x%2==0])
s3 = set([x for x in range(1,21) if x%3==0])
s4 = set([x for x in range(1,21) if x%4==0])
print (s2)
print (s3)
print (s4)

print (s3.issubset(s2))
print(s4.issubset(s2))


#Create a set with the letters in ‘Python’ and add ‘i’ to the set.

str1 = 'python'
set_python = set(str1)
print (set_python)
set_python.add('i')
print (set_python)

#Create a frozenset with the letters in ‘marathon’.

set_marathon = frozenset('marathon')
print (set_marathon)
#display the union and intersection of the two sets.

set_union = set_python.union(set_marathon)
set_inter = set_python.intersection(set_marathon)
print (set_union)
print(set_inter)


