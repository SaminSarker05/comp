"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        return self.helper(grid, 0, 0, len(grid))

    def helper(self, grid, i, j, n):

        flag = True

        # 0. check if all same value within grid range
        for x in range(i, i + n):
            for y in range(j, j + n):
                if grid[x][y] != grid[i][j]:
                    flag = False
                    break
        
        # 1. if all same return node per instruction
        if flag: return Node(val=grid[i][j], isLeaf=True)

        # 2. otherwise make recursive calls
        root = Node(grid[i][j], False)

        # 3. in recursive call split grid into quadrants
        root.topLeft = self.helper(grid, i, j, n // 2)
        root.topRight = self.helper(grid, i, j + n // 2, n // 2)
        root.bottomLeft = self.helper(grid, i + n // 2, j, n // 2)
        root.bottomRight = self.helper(grid, i + n // 2, j + n // 2, n // 2)

        return root