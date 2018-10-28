import random
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

    for i in range(len(words)-2):
        if tuple(words[i:i+2]) in trigrams:
            trigrams[tuple(words[i:i+2])].append(words[i + 2]) 
        else: 
            trigrams[tuple(words[i:i+2])] = [words[i + 2]]

    return trigrams

def build_text(trigrams):
    """
    create a new story from the existing words

    takes the trigrams dictionary and return a list with new text
    """
    next_key = random.choice(list(trigrams))
    print(next_key)
    new_creation = list(next_key)
    print(new_creation)

    while True:
        new_creation.append(random.choice(trigrams[next_key]))
        print(new_creation)
        if tuple(new_creation[-2:]) in trigrams and tuple(new_creation[-2:]) != next_key:
            next_key = tuple(new_creation[-2:])
        else:
            break
    
    return new_creation




if __name__ == "__main__":
    
    word_pairs = build_trigrams(words)

    new_text = build_text(word_pairs)

    print(new_text)
    print(" ".join(new_text))