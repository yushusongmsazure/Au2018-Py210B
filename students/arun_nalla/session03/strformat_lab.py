#!usr/bin/env python
#task1

s = ( 2, 123.4567, 10000, 12345.67)
print (s)
''' produce first char as file ext, 2nd as floating with two decimal
 3rd as exponential value with two decimal'''
s1 = ('(file_00{}: {:.2f}, {:.2e}, {:.2e})'.format(*s))
print ("Task1: ", s1)


#task2
# alternative formating
s2 = '(file_00%s : %.2f, %.2e, %.2e)'%s
print ('Task2')
print ("Task2: ", s2)
s3 = f"(file_00{s[0]}: {s[1]:.2f}, {s[2]:.2e}, {s[3]:.2e})"
print ("Task2: ", s3)

#Task3
s4 = ('xyz', 15, 11,60, 200,20)
l = len(s4)
num = ', '.join(["{}"]*l)
s6 = ('The {} number are: '+ num).format(l,*s4)
print ("Task3: ", s6)

#task4
t = ( 4, 30, 2017, 2, 27)

t1 = ("'{:02d} {} {} {:02d} {}'").format(t[3],t[4],t[2],t[0],t[1])

print ("Task4: ", t1)

#task5
my_list= ['oranges', 1.3, 'lemons', 1.1]

s= f'The weight of {my_list[0]} is {my_list[1]} and the weight of {my_list[2]} is {my_list[3]}'
s1_2 = f'The weight of {my_list[0].upper()} is {my_list[1]*1.2} and the weight of {my_list[2].upper()} is {my_list[3]*1.2}'

print ("Task5: ",s)
print ("Task5: ",s1_2)

#Task6