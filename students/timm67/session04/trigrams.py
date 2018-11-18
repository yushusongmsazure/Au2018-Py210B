#!/usr/bin/env python3

import random

sample_words = "I wish I may I wish I might".split()

trigrams = {}

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers

    From example: 

    trigrams = {
        "I wish": ["I", "I"],
        "wish I": ["may", "might"],
        "I may": ["I"],
        "may I": ["wish"],
    }
    """
    global trigrams

    #
    # (word0, word1) ==> word2 
    # If key exists, then append word2 to the list
    #

    for i in range(0, len(words)-2, 1):
        key = (words[i], words[i+1])
        if key in trigrams.keys():
            trigrams[key].append(words[i+2])
        else:
            trigrams[key] = [words[i+2]]
    return trigrams

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
            line = fd.readline()
            while(line):
                line = line.rstrip('/n')
                line.strip('.,:;-?')
                line_list.append(line)
                line = fd.readline()
    except FileNotFoundError:
        print("File [{0}] not found".format(input_filename))
        return None
    except IOError:
        print("I/O Error on file [{0}]".format(input_filename))
        return None
    return line_list


if __name__ == "__main__":
    trigrams = build_trigrams(sample_words)
    print(trigrams)
    random_txt = generate_text_trigrams(trigrams)
    print(random_txt)