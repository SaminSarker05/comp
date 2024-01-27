class Solution(object):
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        islands = 0

        def helper(r, c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == "1":
                grid[r][c] = "0"
                helper(r+1, c)
                helper(r-1, c)
                helper(r, c+1)
                helper(r, c-1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    islands += 1
                    helper(i, j)

        return islands