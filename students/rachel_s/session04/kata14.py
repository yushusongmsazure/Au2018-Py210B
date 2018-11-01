#!/usr/bin/env python3

import string
import re
import random
import sys

def gutenberg_make_words(filename):
    with open(filename) as f:
        output = []
        found_start = False
        for line in f.readlines():
            if not found_start:
                if "***" in line:
                    found_start = True
            else:
                if "***" in line:
                    break
                line = re.findall(r"[\w']+|[.,!?;]", line.lower().strip()
                .replace("\n", " "))
                output += line
    return output

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if not pair in trigrams:
            trigrams[pair] = [follower]
        else:
            trigrams[pair].append(follower)
    return trigrams


def build_text(word_pairs):
    output = []
    for i in range(10):
        starter = start_sentence()
        make_sentence(output, starter)
    
    return output

def start_sentence():
    starters = list(filter(lambda tup: tup[0] == ".",  word_pairs.keys()))
    return random.choice(starters)


def make_sentence(output, pair):
    if pair[1] == ".":
        output.append(pair[1])
    else:
        output.append(pair[1])
        new_pair = (pair[1], random.choice(word_pairs.get(pair)))
        make_sentence(output, new_pair)



if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    words = gutenberg_make_words(filename)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    output = ""
    for word in new_text:
        if word in [".", ",", "!", "?", ";"]:
            output += word
        else:
            output += " "
            output += word

    print(output)