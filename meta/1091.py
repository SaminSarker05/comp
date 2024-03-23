class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # 1. if path undefined return -1
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        d = deque()
        n = len(grid)
        d.append((0, 0, 1))
        # 2. list to store possible directions
        di = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1) ]

        # 3. BFS approach with deque
        while d:
            i, j, path = d.popleft()
            if i == j == n-1:
                # 4. if equal to bottom right return path len
                return path
            for dx, dy in di:
                dnx, dny = i + dx, j + dy
                # 5. check if valid coor and == 0
                if 0 <= dnx < n and 0 <= dny < n and grid[dnx][dny] == 0:
                    # 6. set to 0 to prevent revisit
                    grid[dnx][dny] = 1
                    d.append((dnx, dny, path + 1))
        
        return -1


        