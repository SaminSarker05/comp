# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 1. dfs approach
        def dfs(node, flag):
            if not node:
                return 0
            # 2. use flag to know if a left sided node
            if node.left is None and node.right is None and flag:
                return node.val
        
            l = dfs(node.left, True)
            r = dfs(node.right, False)

            # 3. return of left nodes in enture tree
            return l + r
        
        return dfs(root, False)
        
