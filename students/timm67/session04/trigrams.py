#!/usr/bin/env python3

words = "I wish I may I wish I might".split()

trigrams = None

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    # build up the dict here!
    for i in range(0, len(words)-2, 1):
        key = (words[i], words[i+1])
        key2 = (words[i+1], words[i])
        if key in trigrams.keys():
            trigrams[key] = words[i+2]
        elif key2 in trigrams.keys():
            trigrams[key2] = words[i+2]
        else:
            trigrams[key] = words[i+2]
    return trigrams


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)