class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        """
        Optimized : only need to identify which nodes are isolated. if a node can
        be reached from another node then doesnst contribute to solution set. Can do this by
        tracking which nodes have parents an returning nodes that do not. Isolated nodes
        have paths to other nodes but not to themselves, hence part of solution
        """
        forest = [False] * n

        for n1, n2 in edges:
            # 1. mark that node has a parent
            # 2. can be reached from another node
            forest[n2] = True
        
        res = []
        for i in range(n):
            # 3. add all isolated nodes
            # 4. nodes that cant be reached from another
            if not forest[i]:
                res.append(i)
        
        return res


        # BRUTE FORCE passed
        forest = [i for i in range(n)] 
 
        def find(n):
            if n != forest[n]:
                forest[n] = find(forest[n])
            # 0. path compression optimization
            return forest[n]
        
        # 1. set ancestor of second to root of first
        def union(n1, n2):
            r1 = find(n1)
            forest[n2] = r1
        
        # 2. map provided edges
        for n1, n2 in edges:
            union(n1, n2)

        res = []
        # 3. return all nodes that only map to themselves, i.e cant be reached from another node
        for i in range(n):
            if forest[i] == i:
                res.append(i)
        
        return res