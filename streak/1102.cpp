class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # simulation ? 
        grid = [[0 for i in range(n)] for j in range(m)]
        walls = set([(x, y) for x,y in walls])

        # TLE
        for p, q in guards:
            x, y = p + 1, q
            while (0 <= x < m and 0 <= y < n) and (x, y) not in walls:
                grid[x][y] = -1
                x += 1
            x, y = p - 1, q
            while (0 <= x < m and 0 <= y < n) and (x, y) not in walls:
                grid[x][y] = -1
                x -= 1
            x, y = p, q + 1
            while (0 <= x < m and 0 <= y < n) and (x, y) not in walls:
                grid[x][y] = -1
                y += 1
            x, y = p, q - 1
            while (0 <= x < m and 0 <= y < n) and (x, y) not in walls:
                grid[x][y] = -1
                y -= 1
            
            grid[p][q] = 1
        
        # for row in grid:
        #     print(row)
        
        res = 0

        for i in range(m):
            for j in range(n):
                if (i, j) in walls: continue
                if grid[i][j] == 0:
                    res += 1
        
        return res





        
