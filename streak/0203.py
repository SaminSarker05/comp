class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # needs to be increasing, decreasing, increasing
        # unique p and q for a sol
        p, q = 1, 1
        n = len(nums)
        while p < n and nums[p] > nums[p - 1]:
            p += 1
        if p == q:
            return False
        q = p
        while p < n and nums[p] < nums[p - 1]:
            p += 1
        if p == q:
            return False
        q = p
        while p < n and nums[p] > nums[p - 1]:
            p += 1
        if p == q:
            return False
        
        return p == n
        
