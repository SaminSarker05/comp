class Solution(object):
    def minSubArrayLen(self, target, nums):
        if nums[0] >= target: return 1

        l = 0
        running = nums[0]
        res = float('inf')
        for r in range(1, len(nums)):
            running += nums[r]
            while running >= target and l <= r:
                res = min(res, r - l + 1)
                running -= nums[l]
                l += 1

        if res == float('inf'): return 0
        return res

"""
- sliding window 
- see if you can do better each incrementation
"""