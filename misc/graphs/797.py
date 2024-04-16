class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        store = {}
        res = []
        # 1. store directed edges in hashmap
        for i in range(len(graph)):
            store[i] = graph[i]

        # 2. recursive dfs to find end of path
        def dfs(n, path):
            # 3. if path found add to result array
            if n == len(graph) - 1:
                res.append(path[:])
            else:
                # 4. otherwise recursively call each edge node
                for node in store[n]:
                    path.append(node)
                    dfs(node, path)
                    path.pop()

        dfs(0, [0])

        return res
