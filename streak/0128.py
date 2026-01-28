class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # dp finding minimum dist to each cell will be val of cell + min of left or above cell
        # 2d dp

        # track the coordinates of each cell value
        valLoc = defaultdict(list)
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                valLoc[grid[i][j]].append((i, j))

        dp = [[float('inf') for i in range(n)] for j in range(m)]
        dp[0][0] = 0

        # run dp algo without teleportation
        def dpalgo():
            for i in range(m):
                for j in range(n):
                    val = grid[i][j] + min(
                        dp[i - 1][j] if i else float('inf'),
                        dp[i][j - 1] if j else float('inf')
                    )
                    if val < dp[i][j]:
                        dp[i][j] = val
        
        dpalgo()
        for row in dp:
            print(row)

        keys = sorted(valLoc.keys(), reverse=True)
        for _ in range(k):
            # propogate minimum dp val across higher to lower cells
            dist = float('inf')
            for key in keys:
                # find minimum dist to reach a cell of this val
                for i, j in valLoc[key]:
                    dist = min(dist, dp[i][j])
                # set all cells with this val to that dist --> logically equivalent to a teleportation
                for i, j in valLoc[key]:
                    dp[i][j] = dist
            dpalgo()

        # return min cost to reach bottom right cell
        return dp[-1][-1]




        # WE CAN model this as a djikistra problem but less intutuit ve and indirect
        # we are not given an explicit graph
        # can sort of mapp question to djikstra -- guarentees shortest path in graph with pos weights
        # small constraints
        # for teleportation, dst cell must have a val <= src cell
        # need to KNOW which cells have val <= curr

        # djikstar works but TLE, dense GRAPH
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf') for i in range(n)] for j in range(m)]
        dist[0][0] = 0

        pq = [(0, 0, 0, k)]  # (cost, xcor, ycor)

        while pq:
            cost, x, y, teleports = heapq.heappop(pq)
            if cost > dist[x][y]:  # skip suboptimal path
                continue
            if x == m - 1 and y == n - 1:
                return cost

            if x + 1 < m:  # try move down
                if cost + grid[x + 1][y] < dist[x + 1][y]:
                    dist[x + 1][y] = cost + grid[x + 1][y]
                    heapq.heappush(pq, (cost + grid[x + 1][y], x + 1, y, teleports))
            
            if y + 1 < n:  # try move right
                if cost + grid[x][y + 1] < dist[x][y + 1]:
                    dist[x][y + 1] = cost + grid[x][y + 1]
                    heapq.heappush(pq, (cost + grid[x][y + 1], x, y + 1, teleports))
            
            # try teleport, brute force search of valid teleport locations
            # track three different states
            if teleports:
                # print("yes")
                for i in range(m):
                    for j in range(n):
                        if i == x and j == y:
                            continue
                        if grid[i][j] <= grid[x][y]:
                            # if i == m - 1 and j == n - 1:
                                # print("yipeee")
                                # print(cost, grid[i][j])
                            if cost < dist[i][j]:
                                dist[i][j] = cost
                                heapq.heappush(pq, (cost, i, j, teleports - 1))
                
        return -1


