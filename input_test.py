# print ('Enter your number:')
# x = input()
# print('Your number is ' + x)

# Below is my version of this solution
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
    
    print("what is your input")
    x = int(input())
    print(x)
    isPalindrome(x)

    