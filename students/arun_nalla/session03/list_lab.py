#!usr/bin/env python
# Series 1
# Create a list containing fruits and print the list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print (fruit_list)
# users input to add a fruit, add the fruit to list and print list
response = input('Please add a fruit of your interest\n>>> ').title()
fruit_list.append(response)
print (fruit_list)
number = int(input('Please enter a number either greater than 0 but should be less than the number of items to know the place of the fruit in the list: '))
if number ==0 or number>=len(fruit_list):
    print ('Please enter a number that is less than or equal to {}'.format(len(fruit_list)))
else:
   print ('In the "{}" pythonic position you have "{}".'.format(number, fruit_list[number-1]))

# add a fruit using '+' sign

fruit_list = ['Grape'] + fruit_list
print ("Addition of grape: \n",fruit_list)
fruit_list.insert(0,'Mango')
for i in fruit_list:
    if i.startswith('P'):
        print (i)

#Series2

print (fruit_list)
fruit_list.remove(fruit_list[-1])
print (fruit_list)
del_fruit = input("Remove a fruit\n>>> ").title()
fruit_list .remove(del_fruit)
print (fruit_list)

#series 3 (not as requested but same output)
count =0
while count<1:
    count+=1
    list_fruit = []
    for fruit in fruit_list:
        user_likes = input("Do you like {}:\nif yes enter Y\nif no enter N:\n".format(fruit)).upper()
        if user_likes == 'N':
            pass
        elif user_likes == 'Y':
            list_fruit.append(fruit)
        else:
            print ('Please enter either yes or no')
            user_likes = input("Do you like {}:\nif yes enter Y\nif no enter N:\n".format(fruit)).upper()
fruit_list=list_fruit

print (fruit_list)
#series 4
# make a copy of the original list and reverse the letters in the new list
rev_list_fruits = []
for fruit in fruit_list:
    rev_fruit = fruit[::-1]
    rev_list_fruits.append(rev_fruit)
print (fruit_list[:-1]) # del last item from the original
print (rev_list_fruits)
