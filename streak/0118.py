class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # BFS djikstra; path to all coordinates initially infinity ? TLE
        q = deque([(0, 0)])
        m = len(grid)
        n = len(grid[0])

        # store costs to each coordinate in grid
        store = [[float('inf') for i in range(n)] for j in range(m)]
        store[0][0] = 0 # cost of start coordinate is 0

        while q:
            x, y = q.popleft()  # process position with lowest cost first
            if x == m - 1 and y == n - 1: return store[x][y]
        
            for d, nx, ny in [(1, x, y + 1), (2, x, y - 1), (3, x + 1, y), (4, x - 1, y)]:
                new_cost = store[x][y] + (d != grid[x][y])

                # if lesser cost to grid position then consider
                if 0 <= nx < m and 0 <= ny < n and new_cost < store[nx][ny]: # if within bounds then continue
                    if d == grid[x][y]: q.appendleft((nx, ny)) # prioritize if same direction of grid arrow
                    else: q.append((nx, ny))
                    store[nx][ny] = new_cost    
