"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 
then it does not count towards the sum and values to its right do not count. 
So for example, if b is 13, then both b and c do not count.
"""
#  My solution
# Basically just check if any of the vars are 13, if they are set others accordingly
# Finally, add to sum. 
def lucky_sum(a, b, c):
  sum = 0;
  if a == 13:
    a = 0
    b = 0
    c = 0
  if b == 13:
    b = 0
    c = 0
  if c == 13:
    c = 0
  sum += a
  sum += b
  sum += c
  return sum