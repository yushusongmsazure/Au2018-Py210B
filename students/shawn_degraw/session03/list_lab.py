#Series 1
# setting up the fruit list
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print("This is the fruit list for series 1: {}".format(fruit_list))

# adding user fruit to list
user_input = input("What fruit would you like to add? ")

fruit_list.append(user_input)

print("This is the new fruit list: {}".format(fruit_list))

# print fruit number requested by user
fruit_number = input("What fruit number would you like to see? ")

print("Here is your fruit: {}\n".format(fruit_list[int(fruit_number)-1]))

#add more fruit to the beginning of the list
fruit_list = ["Strawberries"] + fruit_list

print("This is the new fruit list after '+': {}".format(fruit_list))

fruit_list.insert(0, "Kiwi")

print("This is the new fruit list after insert: {}\n".format(fruit_list))

# print all fruits that start with P
print("These are the fruits that start with 'P': ")
for fruit in fruit_list:
    if fruit.startswith("P"):
        print(fruit)

#Series 2
print("This is the fruit list for series 2: {}\n".format(fruit_list))

fruit_list = fruit_list[:-1]

print("This is the fruit list after removing last element: {}\n".format(fruit_list))

# loop until user provides a valid fruit to delete
while True:

    fruit_to_delete = input("What fruit would you like to delete? ")

    if fruit_list.count(fruit_to_delete):
        fruit_list.remove(fruit_to_delete)
        print("This is the fruit list after removing the requested fruit: {}\n".format(fruit_list))
        break
    else:
        print("Fruit not found.\n")

