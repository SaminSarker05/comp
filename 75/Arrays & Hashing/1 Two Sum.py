'''
time complexity: O(n) 
space complexity: O(n) - at worst pushing n numbers to hashtable
'''

class Solution(object):
    def twoSum(self, nums, target):

        seen = {}
        # keep track of seen values and indices
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i
        