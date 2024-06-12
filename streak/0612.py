class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 0. store frequency of each num
        freq = {0: 0, 1: 0, 2: 0}
        for num in nums: freq[num] += 1
        # 1. alter each pos in array
        for pos in range(len(nums)):
            if freq[0] > 0:
                nums[pos] = 0
                freq[0] -= 1
            elif freq[1] > 0:
                nums[pos] = 1
                freq[1] -= 1
            else:
                nums[pos] = 2
                freq[2] -= 1
