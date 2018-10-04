#first_last6
def first_last6(nums):
  return (nums[0] == 6) or (nums[len(nums)-1] == 6)

#common_end
def common_end(a, b):
  return (a[0] == b[0]) or (a[len(a)-1] == b[len(b)-1])

#reverse3
def reverse3(nums):
  newlist = [nums[2], nums[1], nums[0]]
  return newlist

#middle_way
def middle_way(a, b):
  new = [a[1], b[1]]
  return new

#same_first_last
def same_first_last(nums):
  if len(nums) >= 1:
    return nums[0] == nums[len(nums) - 1]
  return False

#sum3
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

#max_end3
def max_end3(nums):
  if nums[0] < nums[2]:
    nums[0] = nums[2]
    nums[1] = nums[2]
    return nums
  else:
    nums[2] = nums[0]
    nums[1] = nums[0]
    return nums

#make_ends
def make_ends(nums):
  newlist = [nums[0], nums[len(nums)-1]]
  return newlist

#make_pi
def make_pi():
  new = [3,1,4]
  return new

#rotate_left3
def rotate_left3(nums):
  newlist = [nums[1], nums[2], nums[0]]
  return newlist

#sum2
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]

#has23
def has23(nums):
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3

