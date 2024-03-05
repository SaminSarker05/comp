class Solution(object):
    def numIslands(self, grid):

        m, n = len(grid), len(grid[0])

        def graph(i, j, visit):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1" and (i, j) not in visit:
                visit.add((i, j))
                grid[i][j] = "#"
                graph(i+1, j, visit)
                graph(i-1, j, visit)
                graph(i, j+1, visit)
                graph(i, j-1, visit)
            

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    graph(i, j, set())
        return res