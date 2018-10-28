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

"""
    for i in range(len(words)-2):
        if trigrams.get(tuple(words[i:i+2])):
            trigrams[tuple(words[i:i+2])].append(words[i + 2]) 
        else: 
            trigrams[tuple(words[i:i+2])] = [words[i + 2]]
    

    for i in range(len(words)-2):
        if trigrams.get((words[i],words[i+1])):
            trigrams[(words[i],words[i+1])].append(words[i + 2])
        else:
            trigrams[(words[i],words[i+1])] = [words[i + 2]]
"""









if __name__ == "__main__":
    
    print(build_trigrams(words))