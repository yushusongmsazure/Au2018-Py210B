

# Task One
seq01 = (2, 123.4567, 10000, 12345.67)
'file_{:0>3d} :    {:.2f}, {:.2e}, {:.2e}'.format(*seq01)

# Task Two
f'file_{seq01[0]:03} :    {seq01[1]:.2f}, {seq01[2]:.2e}, {seq01[3]:.2e}'


# Task Three
seq02 = (1.1,2,3,4,5)
def formatter(in_tuple):
    l = len(in_tuple)
    return ('the {} numbers are: ' + ', '.join(['{}'] * l)).format(l, *in_tuple)
print(formatter(seq02))

# Task Four
seq03 = [4,30,2017,2,27]
'{4:0>2d} {3:0>2d} {2:0>2d} {0:0>2d} {1:0>2d}'.format(*seq03)

# Task Five
fruit01 ='oranges'
weight_fruit1 = 1.3
fruit02 = 'lemons'
weight_fruit2 = 1.1
f"The weight of an {fruit01} is {weight_fruit1} and the weight of a {fruit02} is {weight_fruit2}"

# Task Six A
name_tbl = [['Sam', 13, 10],['Bob', 82, 750],['Jim', 9, 8875],['Tim', 54, 1222.99]]
print('{:^10}|{:^5}|{:^10}'.format('Name','Age','Cost'))
for x in name_tbl:
     print('{:^10}|{:>5}|${:>8.2f}'.format(x[0], x[1], x[2]))

# Task Six B
tup = [1,2,3,4,5,6,7,8,9,10]
print (' '.join(['{: >5d}'.format(x) for x in tup]))





