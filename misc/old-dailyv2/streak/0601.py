class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        # 0. use two pointers at opposite ends of stirng
        while l < r:
            # 1. swap the values at each index
            s[l], s[r] = s[r], s[l]
            # 2. increment pointers; stop loop when l <= r
            l += 1
            r -= 1
            
