# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 1. depth first search algorithm
        def dfs(l, r):
            # 2. check that both left and right nodes exist
            if not l and not r:
                return True
            if not l or not r:
                return False
            # 3. recursively check match between left and rights for mirror
            return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root.left, root.right)
