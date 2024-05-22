class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == 0: return 0



        even, odd = 0, 0
        for n in nums:
            t = max(n + even, odd)
            odd = even
            even = t
        
        return odd
        