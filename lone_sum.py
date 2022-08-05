"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, 
it does not count towards the sum.
"""

# So this one is made a little bit easier by the in function
# To solve this we basically just create a sum function
# Then we say add each var to this sum function as long as it's not
# In a list of bc/ab, etc. 
# So if a = 4, if 4 is not in an array of b or c, then add it because its not a duplicate.
def lone_sum(a, b, c):
  sum = 0
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum;