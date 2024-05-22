from collections import deque

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        if n == 2:
            return 2

        seen = [-1] * (n+1)
        
        def dfs(n):

            if n < 0:
                return 0
            if n == 0:
                return 1
            if seen[n] != -1:
                return seen[n]
            seen[n] = dfs(n-1) + dfs(n-2)

            return seen[n]
        return dfs(n)









        


