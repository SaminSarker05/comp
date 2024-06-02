class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # TOPOLOGICAL SORT
        # 0. ordering nodes such that prerequisites appear before

        # 1. build adjaceny list where each list is classes that have a prequsiote of that index
        adj_list = [[] for x in range(numCourses)]
        n_degree = [0] * numCourses
        # 2. update ndegree of each class or # of prequisites 
        for clas, pre in prerequisites:
            adj_list[pre].append(clas)
            n_degree[clas] += 1
        
        res = []
        q = deque()
        # 3. if ndegree is 0 then add to queue
        for i in range(numCourses):
            if n_degree[i] == 0: q.append(i)

        # 4. traverse through nodes and decrement ndegree of each connected nodes
        while q:
            node = q.popleft()      
            res.append(node)
            # exploring all classes with prerequisite of node
            for n in adj_list[node]:
                n_degree[n] -= 1
                if n_degree[n] == 0: q.append(n)
        
        # 5. if total length of topological sort doesnt match numCourses than no valid order
        return res if len(res) == numCourses else []