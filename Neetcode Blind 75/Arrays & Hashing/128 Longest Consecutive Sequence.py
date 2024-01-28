'''
time complexity: O(n) 
space complexity: O(n) - length of nums
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)
        
        # optimized brute force method of checking if each increment exists
        numbers = set(nums)
        res = 1
        for num in nums:
            if num-1 not in numbers:
                search = num + 1
                total = 1

                while search in numbers:
                    total += 1
                    search += 1
                
                res = max(res, total)

        return res    