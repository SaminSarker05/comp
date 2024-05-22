'''
time complexity: O(n) 
space complexity: O(n) - at worst pushing n numbers to hashtable
'''

class Solution(object):
    def twoSum(self, nums, target):

        mapp = {}

        for i in range(len(nums)):
            look = target - nums[i]
            if look in mapp: return [i, mapp[look]]
            mapp[nums[i]] = i
        
        return -1

"""
- hashmap will hold values passed and their indices
- if difference in hashmap then pair found to sum to target
"""