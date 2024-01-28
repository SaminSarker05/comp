'''
time complexity: O(n) 
space complexity: O(n)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # calculate prefix and suffix and then multiply

        if len(nums) == 2:
            return nums[::-1]

        prefix, suffix = [1], [1]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i-1])

        for i in range(len(nums) - 1, 0, -1):
            suffix.append(suffix[-1] * nums[i])

        for j in range(len(suffix)):
            prefix[j] *= suffix[len(suffix) - j - 1]

        return prefix