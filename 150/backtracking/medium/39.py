class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        # 0. dfs algo to loop through all possible unique combinations
        def dfs(ind, running):
            if sum(running) == target:
                res.append(running[:])
                return
            if sum(running) > target: return
            for i in range(ind, len(candidates)):
                running.append(candidates[i])
                # 1. recursive call passes in current index so doest repeat past values
                dfs(i, running)
                running.pop()
        dfs(0, [])
        return res