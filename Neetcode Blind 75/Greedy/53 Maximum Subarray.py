class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        running = 0
        for n in nums:
            if running < 0:
                running = 0
            running += n
            res = max(res, running)
        return res
        


        