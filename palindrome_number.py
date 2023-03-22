# Given an integer x, return true if x is a palindrome, and false otherwise.
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         rev = 0
#         orig = x
#         while x != 0:
#             rev = rev * 10 + x % 10
#             x //= 10
#         return rev == orig

# New solution that is more understandable for me
# Convert to String
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         string = str(x)
#         left = 0
#         right = len(str) - 1

#         while left < right:
#             if string[left] != string[right]:
#                 return False
            
#             left += 1
#             right -= 1

#             return True

#  My personal solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        left = 0
        right = len(str) - 1

        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1

            return True