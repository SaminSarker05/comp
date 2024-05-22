class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            if n in seen: return False
            seen.add(n)
            d = n
            n = 0
            while d != 0:
                n += (d % 10) ** 2
                d /= 10
        return True

"""
- use set to track if cycle emerges, then return false
- recalculate n using modulue and division operators
"""