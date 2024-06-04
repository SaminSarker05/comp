class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 0. base cases
        if n == 0: return []
        if n == 1: return ["()"]

        res = []
        k = n * 2

        # 1. dfs algo to add left right paren
        def dfs(x, y, running):
            # 2. if length reached then add to res
            if len(running) == k:
                res.append(running)
                return
            # 3. if left paren count exists then add
            if x:
                # 4. decrement left parent count and add to running
                dfs(x - 1, y, running + "(")
            # 5. if only more right paren then add to be unique
            # ensure parenthesis are valid
            if y > x:
                dfs(x, y - 1, running + ")")
        dfs(n, n, "")
        return res

        