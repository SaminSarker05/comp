class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        def backtrack(n, path):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(n, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()
            
        backtrack(0, [])
        return res