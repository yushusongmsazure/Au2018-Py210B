#! usr/bin/env python 3
import random
import string
from collections import defaultdict

#words = 'I wish I may I wish I might'.split()
def trigram_dict (words):
    trilist = defaultdict(list)
    for i in range(len(words)-2):
        a = tuple(words[i:i+2])
        b = words[i+2]
        trilist[a].append(b)
        """if a not in trilist:
            trilist[a] = [b]
        else:
            trilist[a].append(b)"""
    return trilist

def new_data(old_data):
    word_list = ''
    with open(filename, 'r') as file_name:
        translator = str.maketrans('','', string.punctuation)
        for lines in file_name.readlines():
            words = lines.translate(translator)
            word_list+=words
    list_of_words = word_list.split()
    return list_of_words

def build_new_story(story):
    trigrams = trigram_dict(words)
    keys_first = random.choice(list(trigrams))
    #print (keys_first, "key first")
    my_list = list(keys_first)
    #print (my_list, "new list")
    my_list.append(random.choice(trigrams[keys_first]))
    #print (my_list, "first full")
    while len(my_list)<=100:
        key_next = tuple(my_list[-2:])
        if key_next in trigrams:
            my_list.append(random.choice(trigrams[key_next]))
        else:
            break
        new_story = ' '.join(my_list)
    return (new_story)

if __name__=='__main__':
    # get the filename from the command line
    try:
        filename = input ("Enter a file name>>>")
    except IndexError:
        print("You must pass in a filename")

    words = new_data(filename)
    word_pairs = trigram_dict(words)
    new_text = build_new_story(word_pairs)
    print (new_text)
