#!/usr/bin/env python3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("{}".format(fruits))
response = input("Enter another fruit to append: ")
fruits.append(response)
print("{}".format(fruits))
index = input("Enter the fruit index: ")
idx = int(index) - 1 # use to index into array
print("fruits[{0}] is {1}".format(index, fruits[idx]))
response = input("Enter another fruit to pre-pend: ")
fruits = [response] + fruits
print("{}".format(fruits))
response = input("Enter another fruit to pre-pend: ")
fruits.insert(0, response)
print("{}".format(fruits))
print("Fruits beginning with P")
for x in fruits[:]:
    if (x[0] == 'P'):
        print("{}".format(x))

# Part 2

