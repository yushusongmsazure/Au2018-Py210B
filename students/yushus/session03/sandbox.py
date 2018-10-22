a_string = "this is a dog"

last = a_string[-1]
first = a_string[0]

print(last)
print(first)

a_string=a_string.replace(a_string[0],a_string[-1]).replace(a_string[-1],a_string[0])
print(a_string)
a_string=a_string.replace(last, first)
#print(a_string)

s='cat is cute'
print(s[::-1])

input('call for help')
