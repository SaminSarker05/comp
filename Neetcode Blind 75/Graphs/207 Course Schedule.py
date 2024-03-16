class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        preMap = {i:[] for i in range(numCourses)}
        for cre, pre in prerequisites:
            preMap[cre].append(pre)

        visited = set()

        def dfs(cre):
            if cre in visited:
                return False
            
            if preMap[cre] == []:
                return True
            
            visited.add(cre)
            for pre in preMap[cre]:
                if not dfs(pre): return False
            visited.remove(cre)
            preMap[cre] = []
            return True
        
        for cre in range(numCourses):
            if not dfs(cre): return False
        return True