#!/usr/bin/env python3
#Week3 Excercise mailroom part 2
#Student: Brandon Nguyen - Au2018
import sys
import unittest



words = "I wish I may I wish I might".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!
    words = "I wish I may I wish I might".split()
    # dictionary = {} concept -> dictionary.setdefault("list", []).append("list_item"): to initilize 
    
    for i in range(len(words)-2): # why -2 : avoiding out of bound via the +2 below???
        pair = tuple(words[i:i + 2]) #list cannot be key! conversion needed.
        follower = words[i + 2]
        trigrams.setdefault(pair,[]).append(follower)
    return trigrams


if __name__ == "__main__":
    trigramTest = {("I", "wish"): ["I", "I"],
            ("wish", "I"): ["may", "might"],
            ("may", "I"): ["wish"],
            ("I", "may"): ["I"],
            }
    assert build_trigrams(words) == trigramTest
    print("test pass")

    trigrams1 = build_trigrams(words)
    print(trigrams1)

'''if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)

'''    