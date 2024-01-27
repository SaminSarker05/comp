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

        dp = [-1] * (n+1)

        def helper(n, dp):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = helper(n-1, dp) + helper(n-2, dp)
            return dp[n]

        return helper(n, dp)