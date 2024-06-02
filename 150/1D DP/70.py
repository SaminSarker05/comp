from collections import deque

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # DP problem

        # 0. base cases
        if n == 1: return 1
        if n == 2: return 2

        # 1. array to hold solutions to each step on staircase
        steps = [-1] * (n + 1)

        def dfs(value):
            # 2. if value becomes negative then solution not found
            if value < 0: return 0
            if value == 0: return 1
            # 3. if problem already solved return that solution
            if steps[value] != -1: return steps[value]
            # 4. if problem not solved make recursive call with 1 and 2 steps
            steps[value] = dfs(value - 1) + dfs(value - 2)
            return steps[value]
        
        return dfs(n)