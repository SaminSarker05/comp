class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # TOPOLOGICAL SORT
        # kahns algorithm for DAG (directed acyclic graph)
        # sorts nodes such that prerequisite nodes appear before NOT UNIQUE
        # start with node where ndegree is 0 - no incoming nodes
        # recursive algo by updating ndegree of nodes each time
        ndegree = [0] * numCourses
        adj_list = [[] for x in range(numCourses)]
        for c in prerequisites:
            clas, pre = c
            adj_list[pre].append(clas)
            # 0. prequisite classes point to a class
            ndegree[clas] += 1
        
        # BFS ALGO
        q = []
        # 1. add all 0 ndegree or no prequisites class to queue
        for i in range(numCourses):
            if ndegree[i] == 0: q.append(i)
        
        # 2. store number of classes visited
        visited = 0
        while q:
            node = q.pop(0)
            visited += 1
            # 3. explore class prequisites and update their ndegrees
            for n in adj_list[node]:
                ndegree[n] -= 1
                # 4. if ndegress of class becomes 0 add to queue to process
                if ndegree[n] == 0: q.append(n)
        
        return visited == numCourses
        

        store = defaultdict(list)
        # 0. building adjacency list to represent graph
        for n1, n2 in prerequisites:
            store[n1].append(n2)
        
        # 1. hashset to mark seen classes and detect schedule cycle
        seen = set()
        def dfs(node):
            # 2. if course has no prerequsiites its a valid course
            if store[node] == []: return True
            # 3. if a course was already seen then cycle
            if node in seen: return False

            # 4. recursive call to classes preqreusites
            seen.add(node)
            for n in store[node]:
                if dfs(n) == False: return False
            
            # 5. remove class since prequisites can overlap
            seen.remove(node)
            store[node] = []
            return True
        
        # 6. loop through array and pass into dfs algo
        for n1, n2 in prerequisites:
            if dfs(n1) == False: return False
        return True
