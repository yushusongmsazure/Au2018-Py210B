# Given a string and a non-negative int n, return a larger string that is n 
# copies of the original string
def string_times(str, n):
    newstr = ''
    for i in range(n):
        newstr += str
    return newstr


# Given a string and a non-negative int n, we'll say that the front of the 
# string is the first 3 chars, or whatever is there if the string is less than 
# length 3. Return n copies of the front;
def front_times(str, n):
    newstr = ''
    if(len(str) <= 3):
        front = str
    else:
        front = str[:3]
    for i in range(n):
        newstr += front
    return newstr


# Given a string, return a new string made of every other char starting with 
# the first, so "Hello" yields "Hlo".
def string_bits(str):
    newstr = ''
    for i in range(len(str)):
        if(i % 2 == 0):
            newstr += str[i]
    return newstr


# Given a non-empty string like "Code" return a string like "CCoCodCode"
def string_splosion(str):
    newstr == ''
    for i in range(len(str)):
        newstr += str[:i]
    return newstr + str