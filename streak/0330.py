class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        l, res = 0, 0
        small, big = -1, -1
        # 1. if num not in bounds update left pointer
        for i, val in enumerate(nums):
            if val < minK or val > maxK:
                l = i + 1
                small = big = -1
            # 2. track if min and max seen
            if val == minK:
                small = i
            if val == maxK:
                big = i
            # 3. if both min and max seen update res
            if small != -1 and big != -1:
                # 4. take min of small big positions to get smallest valid subarray
                res += min(small,big) - l + 1
        return res