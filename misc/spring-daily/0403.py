class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        val = 0
        # 1. ignore characters except parenthesis
        for char in s:
            # 2. if left paren increment total and update max count
            if char == "(":
                val += 1
                res = max(res, val)
            # 3. if right paren decrement total nested 
            elif char == ")":
                val -= 1
            
        return res
        