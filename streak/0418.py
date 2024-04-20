class Solution(object):
    def numIslands(self, grid):

        m, n = len(grid), len(grid[0])

        # 1. dfs graph solution
        def graph(i, j):
            # 2. if land found traverse adjacent coordinates
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                # 3. mark as water to not revisit
                grid[i][j] = "0"
                graph(i+1, j)
                graph(i-1, j)
                graph(i, j+1)
                graph(i, j-1)
            

        res = 0
        # 4. call dfs algo if piece of land found
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    graph(i, j)
        return res