class Solution(object):
    def findDuplicate(self, nums):
        
        # 1. use set to keep track of char frequency
        freq = set()
        for n in nums:
            # 2. if duplicate value return char
            if n in freq:
                return n
            freq.add(n)