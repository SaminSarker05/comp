'''
time complexity: O(n^2) 
space complexity: O(n)
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # three pointer solution
        # search for target 

        nums.sort()
        values = set()

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    values.add((nums[i], nums[j], nums[k] ))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
            
        res = list(values)
        return res
