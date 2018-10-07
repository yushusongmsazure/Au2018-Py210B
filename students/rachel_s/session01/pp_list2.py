# Return the number of even ints in the given array. Note: the % "mod" operator 
# computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count


# Given an array length 1 or more of ints, return the difference between the 
# largest and smallest values in the array. Note: the built-in min(v1, v2) and 
# max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
    biggest = nums[0]
    smallest = nums[0]
    for i in nums:
        biggest = max(biggest, i)
        smallest = min(smallest, i)
    return biggest - smallest


# Return the "centered" average of an array of ints, which we'll say is the 
# mean average of the values, except ignoring the largest and smallest values 
# in the array. If there are multiple copies of the smallest value, ignore just 
# one copy, and likewise for the largest value. Use int division to produce the 
# final average. You may assume that the array is length 3 or more.
def centered_average(nums):
    nums = sorted(nums)
    nums = nums[1:-1]
    return sum(nums) / len(nums)


# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that 
# come immediately after a 13 also do not count.
def sum13(nums):
    my_sum = 0
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] != 13:
            if i == 0:
                my_sum += nums[i]
            else:
                if nums[i-1] != 13:
                    my_sum += nums[i]
    return my_sum


# Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 7 (every 6 will be followed by at 
# least one 7). Return 0 for no numbers.

def sum67(nums):
    i = 0
    my_sum = 0
    i_saw_a_6 = False
    while i < len(nums):
        if i_saw_a_6 == False:
            if nums[i] == 6:
                i_saw_a_6 = True
            else:
                my_sum += nums[i]
        if nums[i] == 7:
            i_saw_a_6 = False
        i += 1
    return my_sum


# Given an array of ints, return True if the array contains a 2 next to a 2 
# somewhere.
def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False


# We want to make a row of bricks that is goal inches long. We have a number of 
# small bricks (1 inch each) and big bricks (5 inches each). Return True if it 
# is possible to make the goal by choosing from the given bricks. This is a 
# little harder than it looks and can be done without any loops.
def make_bricks(small, big, goal):
    if goal % 5 > small:
        return False
    elif small + (big * 5) < goal:
        return False
    else:
        return True


# Given 3 int values, a b c, return their sum. However, if one of the values is 
# the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
    my_sum = 0
    if a != b:
        my_sum = a + b
    if c != b and c != a:
        my_sum += c
    return my_sum


# Given 3 int values, a b c, return their sum. However, if one of the values is 
# 13 then it does not count towards the sum and values to its right do not 
# count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    my_sum = 0
    for i in [a, b, c]:
        if i == 13:
            return my_sum
        else:
            my_sum += i
    return my_sum


# Given 3 int values, a b c, return their sum. However, if any of the values is 
# a teen -- in the range 13..19 inclusive -- then that value counts as 0, 
# except 15 and 16 do not count as a teens. Write a separate helper "def 
# fix_teen(n):"that takes in an int value and returns that value fixed for the 
# teen rule. In this way, you avoid repeating the teen code 3 times (i.e. 
# "decomposition"). Define the helper below and at the same indent level as the 
# main no_teen_sum().
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(num):
    if num in range(13, 20):
        if num == 15 or num == 16:
            return num
        else:
            return 0
    else:
        return num


# For this problem, we'll round an int value up to the next multiple of 10 if 
# its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round 
# down to the previous multiple of 10 if its rightmost digit is less than 5, so 
# 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded 
# values. To avoid code repetition, write a separate helper "def round10(num):" 
# and call it 3 times. Write the helper entirely below and at the same indent 
# level as round_sum().