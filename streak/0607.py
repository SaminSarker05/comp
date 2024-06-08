class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 1: return False

        remain = {0:-1}
        # 0. keep track of remainders and ind in hashtable
        running = 0
        for ind, num in enumerate(nums):
            # 1. update remainder in each iteration
            running = (running + num) % k
            # 2. if remainder seen before check if its index is less than current
            if running in remain:
                if remain[running] < ind - 1: return True
            # 3. if not seen then add to remainder
            else: remain[running] = ind
        return False
