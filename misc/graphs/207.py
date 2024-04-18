class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        
        # PROBLEM REDO

        # 1. dict to hold classes and its requirements:
        store = {i:[] for i in range(numCourses)}
        for key, val in prerequisites:
            store[key].append(val)
        

        # 2. DFS algo to ensure all class requirements can be met
        seen = set() # use set to not revisit a class
        def dfs(key):
            # 3. if no requirements than can do class
            if store[key] == []:
                return True
            
            # 4. if class seen before than cycle
            if key in seen:
                return False
            
            seen.add(key)

            # 5. loop through class requirements 
            for node in store[key]:
                if not dfs(node): return False
            
            seen.remove(key)
            # 6. required optimization for time
            # mark class as succesfull in case of revisit
            store[key] = []
            return True

        for n1, n2 in prerequisites:
            if not dfs(n1): return False
        
        return True



        