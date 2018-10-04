#string_times
def string_times(str, n):
  return str * n

#string_splosion
def string_splosion(str):
  newstr = ""
  for i in range(len(str)):
    newstr += str[:i+1]
  return newstr

#array_front9
def array_front9(nums):
  for i in range(len(nums)):
    if (nums[i] == 9) and i < 4:
      return True
  return False

#front_times
def front_times(str, n):
  if len(str) < 3:
    newstr = str
  else:
    newstr = str[:3]
  return newstr * n

#last2 - directions unclear, what is the substring? Used the last two char as the substring
def last2(str):
  count = 0
  matchstr = str[len(str)-2:]
  for i in range(len(str)-2):
    if matchstr == str[i:i+2]:
      count += 1
  return count

#array123
def array123(nums):
  for i in range(len(nums)-2):
    if [1,2,3] == nums[i:i+3]:
      return True
  return False

#string_bits
def string_bits(str):
  newstr = ""
  for i in range(len(str)):
    if i%2 == 0:
      newstr += str[i]
  return newstr

#array_count9
def array_count9(nums):
  return nums.count(9)

#string_match
def string_match(a, b):
  count = 0
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
