"""

Given three ints, a b c, return True if one of b or c is "close" 
(differing from a by at most 1), while the other is "far",
differing from both other values by 2 or more. Note: abs(num) 
computes the absolute value of a number.
"""
def close_far(a, b, c):
  if (b == a + 1 or a - 1 or a) or (c == a + 1 or a - 1 or a):              #looking for the "close" one
    if ((c > a + 2) and (c > b + 2)) or ((c <= a - 2) and (c <= b - 2)):    #looking for c to be the "far" one
        return True
    elif (b > (a + 2 and c + 2)) or ((b <= a - 2) and (b <= c - 2)):        #looking for b to be the "far" one
        return True
    else:    
      return False
