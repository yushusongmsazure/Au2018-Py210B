#double_char
def double_char(str):
  newstr = ""
  for i in str:
    newstr += (i * 2)
  return newstr

#count_code
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    comparestr = "code"
    nextstr = str[i:i+4]
    if nextstr[0] == "c" and nextstr[1] == "o" and nextstr[3] == "e":
      count += 1
  return count

#count_hi
def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    comparestr = "hi"
    nextstr = str[i:i+2]
    if nextstr == comparestr:
      count += 1
  return count

#end_other
def end_other(a, b):
  lengtha = len(a)
  lengthb = len(b)
  if lengtha > lengthb:
    if a[(lengtha-lengthb):].lower() == b.lower():
      return True
  else:
    if b[(lengthb-lengtha):].lower() == a.lower():
      return True
  return False

