class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # REDO
        res = nums[0]
        running = 0
        for n in nums:
            if running < 0: # if running sum is negative then only decreases possible sum so reset to 0
                # droppoing subarray
                running = 0
            running += n # add current element to runing
            res = max(res, running) # compare current to running subarray
        return res

        # Kadane's algorithm
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
            # print(res)
        return res

