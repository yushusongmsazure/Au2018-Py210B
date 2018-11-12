#!/usr/bin/env python3

import sys
from collections import defaultdict

words = "I wish I may I wish I might".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = defaultdict(list)

    # build up the dict here!

    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        #if tuple(pair) in trigrams:
        trigrams[tuple(pair)].append(follower)
            #list(trigrams[tuple(pair)]).append(follower)
            #trigrams[tuple(pair)] = [trigrams[tuple(pair)], follower]
        #else:
        #    trigrams[tuple(pair)] = [follower]

    return trigrams


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)