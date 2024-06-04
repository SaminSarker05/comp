class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # COMBINATIONS
        # order does matter - must be unique

        # 0. stores all combinations
        res = []

        # 1. recursive algo taking in running array and num to start with
        def dfs(ind, running):
            # 2. if length of k then add to res
            if len(running) == k:
                res.append(running[:])
                return
            # 3. loop through ind to end
            for i in range(ind, n + 1):
                running.append(i)
                # 4. in recursive call increment i to not repeat arrays
                dfs(i + 1, running)
                running.pop()

        dfs(1, [])
        return res
        