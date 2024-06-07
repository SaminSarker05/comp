class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0. base case
        if nums == 0: return 0

        even, odd = 0, 0
        # 1. loop through nums only cases are taking even or odd subsequences
        for n in nums:
            # 2. update even holder to be max
            t = max(n + even, odd)
            odd = even  # 3. update odd to be even
            even = t
        
        return odd