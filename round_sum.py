def round_sum(a, b, c):
  # Return sum of a,b,c 
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  
  # Take the number by modulus 10 if that's greater than
  
  if num % 10 < 5:
    return num - (num % 10)
        
  return num + (10 - num % 10)
    
    
   # If a numbers right most digit is greater than 5. (digit >5)
    # We're rounding an int up to the next multiple of 10
   
    
  # If a numbers rightmost digit is less than 5. (digit < 5)
    # We're rounding it down to the previous multiple of 10.