class Solution(object):
    def numIslands(self, grid):
        # 0. hold the row and col values of the grind
        m = len(grid)
        n = len(grid[0])

        res = 0

        # 1. recursive function to traverse islands
        def traverse(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                # 2. if island set to 0 and explore neighbors
                grid[i][j] = "0"
                traverse(i + 1, j)
                traverse(i - 1, j)
                traverse(i, j + 1)
                traverse(i, j - 1)

        # 3. call traverse if land found and increment island count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1": 
                    res += 1
                    traverse(i, j)
        
        return res