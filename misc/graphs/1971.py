class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """


        # UNION-FIND ALGO

        # 0. every node is root of itself at first
        forest = {i:i for i in range(n)}
        rank = [1] * n # OPTIMIZATION: to keep trees balanced

        # 1. find recursively searches for root, checks if index and node match
        def find(n):
            if n != forest[n]:
                # OPTIMIZATION: path compression
                # if node not found at index make parent be the returned found root
                forest[n] = find(forest[n])
            return forest[n]
        
        def union(n1, n2):
            # 2. get parent nodes of each to combine trees
            r1, r2 = find(n1), find(n2)
            # 3. set root of one tree to other
            if rank[r1] <= rank[r2]:
                forest[r2] = r1
                r1 += 1
            else:
                forest[r1] = r2
                r2 += 1

        for n1, n2 in edges:
            # 4. combine each edge provided
            union(n1, n2)
        
        # 5. if path exists nodes must have same root
        return find(source) == find(destination)




        # DFS ALGO
        if source == destination: return True
        if not edges: return False

        # 1. store maping of vertex and edges in dict
        store = defaultdict(list)
        for n1, n2 in edges:
            store[n1].append(n2)
            store[n2].append(n1)
        
        # 2. recursively look for destination from source
        def dfs(seen, key):
            val = False
            # 3. traverse through key value list
            for node in store[key]:
                if node == destination:
                    return True
                # 4. if not match then use node as key 
                if node not in seen:
                    # 5. track seen nodes in a set
                    seen.add(node)
                    val = val or dfs(seen, node)
            return val
        
        empty = set()
        return dfs(empty, source)
