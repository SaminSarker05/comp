class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)

        nums = set(nums) # O(1) amertized lookup 
        res = 1
        for num in nums:
            if num-1 not in nums:
                search = num + 1
                while search in nums:
                    search += 1
                res = max(res, search - num)
        return res

"""
- look for increasing numbers
- make nums into a set for faster lookup
"""