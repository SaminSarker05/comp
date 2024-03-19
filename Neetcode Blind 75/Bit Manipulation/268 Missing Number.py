class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums) + 1
        real = 0
        actual = 0
        for i in nums: actual += i
        for i in range(total): real += i 
        return real - actual
        