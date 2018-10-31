
import sys

### trigram testing
# words = "I wish I may I wish I might".split()
# wordcnt = 25

#### create dictionary: loop method
# d = {}
# for i in range(len(words)-2):
#     pair = tuple(words[i:i + 2])
#     follower = words[i + 2]  
#     if pair not in d:
#         d[pair] = [follower]
#     else:
#         d[pair].append(follower)

def getfile():
    filename = input("Please provide file path and name: ")
    # filename = "students//jjakub//session04//irving_sleepy_hollow.txt"

    ### open file
    f = open(str(filename))
    book = f.read().replace('\n', ' ')

    ### start and end file text
    start_str = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    end_str = '*** END OF THIS PROJECT GUTENBERG EBOOK'

    ### slice based on start and end file text
    start_indx = book.find(start_str)
    end_indx = book.find(end_str)

    text = book[start_indx + len(start_str) :end_indx + len(end_str)].split()
    return text

def trigram_len():
    n = int(input("Please provide trigram length: "))
    return n

### create dictionary: setdefault method
def build_trigrams(words, wordcnt):
    d = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        d.setdefault(pair,[]).append(follower)

    trigrams = {}
    import random
    trigrams = list(random.choice(list(d.keys())))

    while len(trigrams) < wordcnt:
        cur_pair = trigrams[-2:]
        if tuple(cur_pair) not in d:
            cur_pair = list(random.choice(list(d.keys())))
        trigrams.append(random.choice(d.setdefault(tuple(cur_pair),[])))

    trigrams = ' '.join(trigrams)
    return trigrams

if __name__ == "__main__":
    build_trigrams(getfile(),trigram_len())