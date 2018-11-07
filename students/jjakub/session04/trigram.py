

# words = "I wish I may I wish I might".split()
# wordcnt = 25

# create dictionary: loop method
# d = {}
# for i in range(len(words)-2):
#     pair = tuple(words[i:i + 2])
#     follower = words[i + 2]  
#     if pair not in d:
#         d[pair] = [follower]
#     else:
#         d[pair].append(follower)

### create dictionary
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
        trigrams.extend(d.setdefault(tuple(cur_pair),[]))

    return trigrams

if __name__ == "__main__":
    trigrams = build_trigrams(words, wordcnt)
    print(trigrams)


filepath = '.\\students\\jjakub\\session04\\'
filename = 'sherlock_short.txt'

f = open(str(filepath + filename))
book = f.read()
f.close()

book = book.split()

build_trigrams(book,wordcnt)