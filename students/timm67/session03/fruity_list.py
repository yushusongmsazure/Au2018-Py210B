#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
List Lab
"""

#
# Series 1
#

print("Series 1\n")
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("Original List: {}".format(fruits))
fruits1 = fruits.copy()
response = input("Enter another fruit to append: ")
fruits1.append(response)
print("Appended List: {}".format(fruits1))
index = input("Enter the fruit index: ")
idx = int(index) - 1   # use to index into array
print("fruits[{0}] is {1}".format(index, fruits1[idx]))
response = input("Enter another fruit to pre-pend: ")
fruits1 = [response] + fruits1
print("Pre-pended List: {}".format(fruits1))
response = input("Enter another fruit to pre-pend: ")
fruits1.insert(0, response)
print("Pre-pended List 2: {}".format(fruits1))
print("Fruits beginning with P:")
for x in fruits1[:]:
    if (x[0] == 'P'):
        print("{}".format(x))

#
# Series 2
#

fruits2 = fruits.copy()
print("Series 2\n")
print("Starting List: {}".format(fruits2))
fruits2.remove(fruits2[-1:])
print("Remove last element: {}".format(fruits2))
response = input("Enter a fruit to remove: ")
try:
        fruits2.remove(response)
except ValueError:
        print("Fruit {} not found in list".format(response))

#
# Series 3
#

fruits3 = fruits.copy()
print("Series 3\n")
print("Starting List: {}".format(fruits3))
for f in fruits3:
        print("Do you like {} (yes/no)? ".format(f)) # lowercase?
        response = ""
        while (response != "no") or (response != "yes"):
                response = input()
        if (response == "no"):
                fruits3.remove(f)
print("List after removals: {}".format(fruits3))

#
# Series 4
#

fruits4 = fruits.copy()
print("Series 4\n")
print("Starting List: {}".format(fruits4))
for f in fruits4:
        f = f[::-1] #Extended slice syntax
print("List after item reversal: {}".format(fruits4))
print("Original List before removing last element: {}".format(fruits))
fruits.remove(fruits[-1])
print("Original List after removing last element: {}".format(fruits))
