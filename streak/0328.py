class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = max(nums)
        l, res = 0, 0
        count = 0
        # 1. sliding window to calculate subarrays
        for i in range(len(nums)):
            # 2. if elem = max then increment count
            if nums[i] == target:
                count += 1
            # 3. while valid count increment left pointer
            while count >= k:
                # 4. update res e
                res += len(nums) - i
                if nums[l] == target:
                    count -= 1
                l += 1
        return res