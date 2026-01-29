class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # bfs assumes all edges have equal weight, minimizes path, NOT path cost
        # djikstra good for single source shortest path calculation
        # floyd marshall - dp algo calculating the shortest dist between all pairs of vertices/nodes
        # we will have at most 26 nodes for 26 letters of the alphabet
        # tc is v^3
        # tc of djikstra vs floyd marshal depends on graph size

        """
        floyd marshal
        compute shortest dist between every pair of vertices in graph
            gradually allow more intermediate nodes to appear in path
        1. define a m * m matrix, where m = # of vertices
        2. initialize values with edges in graph, if no edge then inf, if self loop set to 0
        3. loop 1 to k where k is the intermidate node being used, m possible intermidate nodes
            let dp[i][j] = min(dp[i][j], matrix[i][k] + matrix[k][j])
        """

        dist = [[float('inf') for j in range(26)] for i in range(26)]
        for i in range(26):
            dist[i][i] = 0  # set self edge to 0
        
        for src, dst, cost in zip(original, changed, cost):
            s = ord(src) - ord('a')
            d = ord(dst) - ord('a')
            # in case of duplicate edges store least cost
            dist[s][d] = min(dist[s][d], cost)
        
        # main floyd marshal logic
        # consider k intermediate chars
        # after the kth iteration dist[i][j] is shortest path from i to j 
        # using at most 0 to k intermediate nodes
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        tc = 0
        for char, target in zip(source, target):
            if char == target:
                continue

            s = ord(char) - ord('a')
            d = ord(target) - ord('a')
            # if no path between vertices then impossible to translate
            if dist[s][d] == float('inf'):
                return -1
            tc += dist[s][d]

        return tc

        # preprocess data to store all possible conversions of chars in source
        # use hashmap to map chars in source to list of tuples (conversion, cost)

        convertTable = defaultdict(list)

        # adjacent graph
        for i in range(len(original)):
            char = original[i]
            convertTable[char].append((changed[i], cost[i]))
        
        source = list(source)
        # print(convertTable)
        # dfs approach to explore different paths, minimuze cost
        # can i precompute least expensive way to convert one char to another

        # TLE
        def dfs(pos, seen):  # func param is our pos in the src string
            if pos == len(source):
                return 0
            # print(pos, source[pos], seen)

            # if the char does not need to change then skip
            if source[pos] == target[pos]:
                # print("hipee")
                return dfs(pos + 1, set())
            
            # minimum value to conver this char to target
            val = float('inf')
            # try different conversions
            for char, cost in convertTable[source[pos]]:
                # print("---", char, cost)
                if char not in seen:
                    seen.add(char)
                    tmp = source[pos]
                    source[pos] = char
                    val = min(val, cost + dfs(pos, seen))
                    source[pos] = tmp
                    seen.remove(char)
            
            return val
            
        res = dfs(0, set())
        return res if res != float('inf') else -1

