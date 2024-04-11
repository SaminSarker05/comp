class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        running = 0
        # 1. reset max if running sum is negative
        for n in nums:
            if running < 0:
                running = 0
            # 2. add current elem each time to running sum
            running += n
            # 3. update res 
            res = max(res, running)
        return res