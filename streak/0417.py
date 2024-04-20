class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = len(grid)
        col = len(grid[0])

        # 1. traverse grid to find piece of land
        res = 0
        for i in range(row):
            for j in range(col):
                # 2. if land found update res
                if grid[i][j] == 1:
                    # 3. decrease res perimeter if adjacent coors also land 
                    res += 4
                    # 4. only check previos left and top since those already passed
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 2
                    
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2
        
        return res





        