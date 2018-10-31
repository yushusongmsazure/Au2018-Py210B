
#! usr/bin/env python 3

words = 'I wish I may I wish I might'.split()
def trigram_dict (words):
    trilist = {}
    for i in range(len(words)-2):
        a = tuple(words[i:i+2])
        b = words[i+2]
        if a not in trilist:
            trilist[a] = [b]
        else:
            trilist[a].append(b)
    return trilist


import random

import string



def build_new_story(story):
    keys_first = random.choice(list(trigram_dict(words)))
    #print (keys_first, "key first")
    my_list = list(keys_first)
    #print (my_list, "new list")
    my_list.append(random.choice(trigram_dict(words)[keys_first]))
    #print (my_list, "first full")
    while len(my_list)<=100:
        key_next = tuple(my_list[-2:])
        if key_next in trigram_dict(words):
            my_list.append(random.choice(trigram_dict(words)[key_next]))
        else:
            break
        new_story = ' '.join(my_list)
    return (new_story)
def new_data(file_name):
    with open("file_name.txt", 'r') as file:

        translator = str.maketrans(',', string.punctuation)
        for lines in file.readlines():
            words = lines.translate(translator)


    return words

if __name__=='__maim__':
    # get the filename from the command line
    try:
        filename = input ("Enter a file name>>>")
    except IndexError:
        print("You must pass in a filename")

    words = new_data(filename)
    word_pairs = trigram_dict(words)
    new_text = build_new_story(word_pairs)
    print (new_text)




"""print(new_text)
    abc = trigram_dict(words)
    xyz = build_new_story(abc)
    print(abc)
    print(xyz)"""

"""if keys_first in my_list:
        my_list.append(random.choice(trigram_dict(words)[keys_first]))
        print (my_list)
        key_next = tuple(my_list[-2:])
        print (key_next, "next key")
        my_list.append(random.choice(trigram_dict(words)[key_next]))
        print (my_list, "next")
key_next2 = tuple(my_list[-2:])
print(key_next2)
my_list.append(random.choice(trigram_dict(words)[key_next2]))
print (my_list, "next2")"""

