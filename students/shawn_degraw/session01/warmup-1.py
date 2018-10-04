# sleep_in
def sleep_in(weekday, vacation):
    if vacation:
      return True
    elif weekday:
      return False
    else:
      return True

# diff21
def diff21(n):
  if n > 21:
    return (n - 21) * 2
  else:
    return 21 - n

# near_hundred
def near_hundred(n):
  near100 = abs(100 - n)
  near200 = abs(200 - n)
  if near100 <= 10:
      return True
  elif near200 <= 10:
      return True
  else:
      return False

#missing_char
def missing_char(str, n):
  newstr=""
  for i in range(len(str)):
    if i != n:
      newstr += str[i]
  return newstr
#def missing_char(str, n):
#  front = str[:n]   # up to but not including n
#  back = str[n+1:]  # n+1 through end of string
#  return front + back

#monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False
## The above can be shortened to:
##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
## Or this very short version (think about how this is the same as the above)
##   return (a_smile == b_smile)

#parrot_trouble
def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False
#def parrot_trouble(talking, hour):
#  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +

#pos_neg
def pos_neg(a, b, negative):
  if negative and (a < 0 and b < 0):
    return True
  elif not negative and (a < 0 and b < 0):
    return False
  elif not negative and (a < 0 or b < 0):
    return True
  else:
    return False
#def pos_neg(a, b, negative):
#  if negative:
#    return (a < 0 and b < 0)
#  else:
#    return ((a < 0 and b > 0) or (a > 0 and b < 0))

#front_back
def front_back(str):
  if len(str) > 2:
    return str[len(str)-1] + str[1:len(str)-1] + str[0]
  elif len(str) == 2:
    return str[len(str)-1] + str[0]
  else:
    return str

#sum_double
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b

#makes10
def makes10(a, b):
  return (a + b) == 10 or a == 10 or b == 10

#not_string
def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return "not " + str
#if len(str) >= 3 and str[:3] == "not":

#front3
def front3(str):
  if len(str) < 3:
    newstr = str
  else:
    newstr = str[:3]
  return newstr * 3