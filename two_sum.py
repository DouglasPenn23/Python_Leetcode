
nums = [ 1, 2 , 3, 4, 5, 6, 7, 8, 9]
target = 5
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         Create a dictionary
        d = {}
#          For each integer and number that results 
#          from the enumeration of the array
        for i, n in enumerate(nums):
#           Make a var equal to the target - n
            m = target - n
#       If the var is in dictionary
            if m in d:
#         return the dictionary w/ index position of m & then i
                return [d[m], i]
#           Else dictionary with number index = i
            else:
                d[n] = i
    