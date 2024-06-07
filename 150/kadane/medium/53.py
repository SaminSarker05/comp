class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 0. base cases
        if len(nums) == 1: return nums[0]

        def kadane(nums):
            running = nums[0]
            ending_here = 0

            # 0. see if ending at a num in array is better than running sol
            for val in nums:
                ending_here = ending_here + val
                # 1. if better than update running sol
                if ending_here > running:
                    running = ending_here
                # 2. if ending here becomes negative reset to 0 to prevent accumulation of -
                if ending_here < 0:
                    ending_here = 0
            return running
        
        return kadane(nums)