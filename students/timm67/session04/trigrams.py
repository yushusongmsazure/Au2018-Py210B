#!/usr/bin/env python3

import random

sample_words = "I wish I may I wish I might".split()

trigrams = {}

def build_trigrams_list(words_list, trigrams_dict):
    for line_list in words_list:
        build_trigrams(line_list, trigrams_dict)

def build_trigrams(word_list, trigrams_dict):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    #
    # (word0, word1) ==> word2 
    # If key exists, then append word2 to the list
    #

    for i in range(0, len(word_list)-2, 1):
        key = (word_list[i], word_list[i+1])
        if key in trigrams_dict.keys():
            trigrams_dict[key].append(word_list[i+2])
        else:
            trigrams_dict[key] = [word_list[i+2]]

def generate_text_trigrams(trigram_dict):
    random_str = str()
    line_length = 0
    trigram_keys = list(trigram_dict.keys())

    for i in range(len(trigram_dict)):
        rand_key_idx = random.randint(0, (len(trigram_dict)-1))
        print('[{0}] Selecting dict entry {1} of {2}'.format(i, rand_key_idx, len(trigram_dict)))
        first_key = trigram_keys[rand_key_idx]
        random_str += (first_key[0])
        random_str += ' '
        random_str +=(first_key[1])
        random_str += ' '
        first_value = trigram_dict[first_key]
        rand_key_idx = random.randint(0, (len(first_value)-1))
        print('[{0}] Selecting entry value {1} of {2}'.format(i, rand_key_idx, len(first_value)))
        word_values = trigram_dict[first_key]
        random_str += word_values[rand_key_idx]
        line_length += len(random_str)
        if (line_length > 70):
            random_str += '\n'
            line_length = 0
        else:
            random_str += ' '
    return random_str


def parse_input_file(input_filename):
    line_list = []
    try:
        with open(input_filename, 'r') as fd:
            try:
                line = fd.readline()
            except IOError:
                print("I/O Error with file [{0}] on readline".format(input_filename))
                return None
            while(line):
                line = line.rstrip('/n')
                line.strip('.,:;-?')
                line_list.append(line)
                line = fd.readline()
    except FileNotFoundError:
        print("File [{0}] not found".format(input_filename))
        return None
    except IOError:
        print("I/O Error with file [{0}] on open".format(input_filename))
        return None

    for line in line_list:
        line = line.split()

    return line_list


if __name__ == "__main__":
    trigrams_dict = {}
    build_trigrams(sample_words, trigrams_dict)
    print(trigrams_dict)
    random_txt = generate_text_trigrams(trigrams_dict)
    print(random_txt)