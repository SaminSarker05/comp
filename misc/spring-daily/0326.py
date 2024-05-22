class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1. edge case return 0
        if k == 0: return 0

        l, r, res = 0, 0, 0
        prod = 1

        # 2. sliding window to track product
        while r < len(nums):
            prod *= nums[r]
            # 3. if product over k decrement l pointer
            while l < r and prod >= k:
                prod //= nums[l]
                l += 1
            # 4. if prod < k add to res
            if prod < k:
                res += r - l + 1
            r += 1

        return res