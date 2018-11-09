#!/usr/bin/env python3

##################################################
## Author: Jackie Cheung
## Date: 2018/10/30
## Version: 0.1
## Class: Au2018-Py210B
## Description: Trigrams – Simple Text Manipulation (Kata Fourteen: Tom Swift Under Milk Wood)
##################################################

import sys
import random

#words = "I wish I may I wish I might".split()

def read_in_data(filename):
    """
    read text from specified file

    """ 
    with open(filename, 'r') as f:
        in_data = f.read()
    f.closed
    True
    print('in_data: \n', in_data)
    return in_data


def make_words(in_data):
    """
    clean up the special character from the text and split the words properly

    """ 
    words = in_data.translate(in_data.maketrans('', '', '^[!@#$%^&*)(+=.,_-]/'))
    print('words: \n', words)
    return words.split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!

    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        if tuple(pair) in trigrams:
            trigrams[tuple(pair)] = [trigrams[tuple(pair)], follower]
        else:
            trigrams[tuple(pair)] = follower

    return trigrams

def build_text(word_pairs):
    """
    build up the new text from trigrams dict

    """ 
    return word_pairs

'''
if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)
'''

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)