# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 1. BFS algorithm
        if not root: return 0
        d = [(root, 1)]
        while d:
            for _ in range(len(d)):
                curr, path = d.pop(0)
                # 2. when first leaf node found return len of path
                if not curr.left and not curr.right:
                    return path
                if curr.left:
                    d.append((curr.left, path+1))
                if curr.right:
                    d.append((curr.right, path+1))
        
            
        # 1. DFS approach
        def dfs(node, path):
            # 2. if None node then ignore 
            if not node:
                return float('inf')
            # 3. if leaf node return path
            if not node.right and not node.left:
                return path
            # 4. return min path of left and right
            left = dfs(node.left, path+1)
            right = dfs(node.right, path+1)
            return min(left, right)

        return dfs(root, 1)
        
