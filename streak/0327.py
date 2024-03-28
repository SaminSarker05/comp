class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 1. use map to store element frequency
        res, l, r = 0, 0, 0
        store = {i:0 for i in nums}

        # 2. sliding window to find longest subarray
        while r < len(nums):
            # 3. if freq > k increment left pointer and
            #    decrement in map 
            while store[nums[r]] + 1 > k:
                store[nums[l]] -= 1
                l += 1
            
            # 4. recalculate max length and increment in map
            res = max(res, r-l+1)
            store[nums[r]] += 1
            r += 1

        return res