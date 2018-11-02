#!/usr/bin/env python3
#Week3 Excercise mailroom part 2
#Student: Brandon Nguyen - Au2018
import sys
import unittest
import random


words = "I wish I may I wish I might"

def build_trigrams(textInput):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    
    trigrams = {}
    strTx = textInput.split()
    # build up the dict here!"
    # dictionary = {} concept -> dictionary.setdefault("list", []).append("list_item"): to initilize   
    for i in range(len(strTx)-2): # why -2 : avoiding out of bound via the +2 below???
        pair = tuple(strTx[i:i + 2]) #list cannot be key! conversion needed.
        follower = strTx[i + 2]
        trigrams.setdefault(pair,[]).append(follower)
    return trigrams

def build_text(word_pairs_dict):
    #initial set of words
  
    key = random.choice(list(word_pairs_dict))
    the_list_of_words = list(key)
    the_list_of_words.append(random.choice(word_pairs_dict.get(key)))

    #loops thru the second times and so forth
    #newKey=tuple(the_list_of_words[-2:])
    #print(the_list_of_words)
  
    while len(the_list_of_words) < 1000:
        newKey=tuple(the_list_of_words[-2:])
        if newKey in word_pairs_dict:
           the_list_of_words.append(random.choice(word_pairs_dict.get(newKey)))
           #print(word_pairs_dict.get(newKey))
        the_list_of_words.append(random.choice(the_list_of_words)) #if not just add a random word from existing list
    return " ".join(the_list_of_words)
    #return the_list_of_words


def readFile_buildTrigrams(filename_in):
    trigrams = {}
    
    with open(filename_in, 'r') as book:
            newData = (book.read().replace('\n', ' ')).split()

    #book.close()
    for i in range(len(newData)-2): # why -2 : avoiding out of bound via the +2 below???
        pair = tuple(newData[i:i + 2]) #list cannot be key! conversion needed.
        follower = newData[i + 2]
        trigrams.setdefault(pair,[]).append(follower)
    return trigrams

    #return newData


if __name__ == "__main__":
    trigramTest = {("I", "wish"): ["I", "I"],
            ("wish", "I"): ["may", "might"],
            ("may", "I"): ["wish"],
            ("I", "may"): ["I"],
            }
    assert build_trigrams(words) == trigramTest

    #testing basic functions
    #newSTring = build_trigrams(words)
    #new_text = build_text(newSTring)
    #print(new_text)

    #print("test pass")

    # get the filename from the command line passing in by : trigrams_text.py filename.txt
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = readFile_buildTrigrams(filename)  
    new_text = build_text(in_data)
    print(new_text)
    #print(in_data)
