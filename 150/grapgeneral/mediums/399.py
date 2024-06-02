class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        # 0. can build two way directed graph from numerators to denominators

        adj_list = defaultdict(list)

        # 1. build adj_list using equations -> num = [(denom, value), ...] TWO WAY
        for i, eq in enumerate(equations):
            num, denom = eq
            adj_list[num].append([denom, values[i]])
            adj_list[denom].append([num, 1 / values[i]])
        
        # 2. bfs algo to try and reach denom from num -> update weights as we go
        def bfs(src, target):
            # 3. if values not in adj_list value cannot be determined
            if src not in adj_list or target not in adj_list: return -1.0
            q = deque()
            q.append([src, 1]) # holds denom and running weight
            seen = set() # 4. set in case repeating num and denom values
            total = 1
            while q:
                node, weight = q.popleft()
                if node == target: # if target found return total weight or division
                    return weight
                for n, w in adj_list[node]: # otherwise explore other denoms
                    if n not in seen:
                        seen.add(n)
                        q.append([n, weight * w])
            
            return -1

        # 5. list comprehension        
        return [bfs(x, y) for x, y in queries]