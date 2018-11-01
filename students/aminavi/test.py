d = {'name': 'alex', 'score': 43}
d['name']
d['score']


d = {'one:': 1, 'two':2, 'three': 3}
str(d)
d.keys()

d = {}
d['one'] = 1
d['two'] = 2
d['three'] = 3
d['four'] = 4
# str(d)
# d.keys()
# for x in d:
# print(x)
# d.values()
# d
# 'one' in d
# 'five' in d
# 'five' not in d
# d.get('one')
# d.get('five', 'haha')

# for i in d:
#     print(i)

# for i in d.values():
#     print(i)

# d.pop('one')

# d = {}
# d.setdefault('somthing', 'value')
# d['something else'] = 'another value'
# d['another thing'] =  'different value'
# item_copy = d

# set()

# set([1,2,3])

# s = set()

# s.update([1,2,3])

# s = 'This is an arbitrary string'
# s.count('i')


# for i in range(0,21):
#     if i % 12 == 0:
#         print(i)


# words = "I wish I may I wish I might".split()

# def build_trigram(words):
#     d = {}
#     for i in range(len(words)-2):
#         pair = tuple(words[i:i + 2])
#         follower = words[i + 2]    
#         d.setdefault(pair,[]).append(follower)

#     trigrams = {}
#     import random
#     trigrams = list(random.choice(list(d.keys())))

#     wordcnt = 10
#     while len(trigrams) < wordcnt:
#         cur_pair = trigrams[-2:]
#         if tuple(cur_pair) not in d:
#             cur_pair = list(random.choice(list(d.keys())))
#         trigrams.extend(d.setdefault(tuple(cur_pair),[]))
#         return trigrams

#     print(trigrams)






donor_list = {
    'william': [653772.32 , 953772.32,100000],
    'jeff': [8888777.22 ,877.33],
    'paul': [663.23, 43.87 ,1.32],
    'mark': [1663.23, 4300.87, 10432.00],
    'nigel': [5000000 , 10]
    }
