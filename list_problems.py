# Given an array of ints, return True if 6 appears as either the first or last element in the array. 
# The array will be length 1 or more.
def first_last6(nums):
  if 6 == nums[0] or nums[len(nums)-1] == 6:
    return True
  else:
    return False


"""

Given an array of ints length 3, 
figure out which is larger, the first or last 
element in the array, and set all the other elements to 
be that value. 
Return the changed array.
"""
def max_end3(nums):
  if nums[0] > nums[-1]:
    return [nums[0]] * 3
  if nums[-1] > nums[0]:
    return [nums[-1]] * 3
  else:
    return [nums[0]] * 3


""""

Given an array of ints, return the sum of the first 
2 elements in the array. If the array length is less than
 2, just sum up the elements that exist, returning 0 if 
 the array is length 0.
"""
def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) < 2:
    return nums[0]
  else:
    return nums[0] + nums[1]


"""

Given 2 int arrays, a and b, each length 3,
return a new array length 2 containing their middle elements.
"""
def middle_way(a, b):
  return [a[1], b[1]]



