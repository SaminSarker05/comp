# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        # 0. dfs algo to check if each node val in valid range
        def dfs(node, left, right):
            # 1. if none return True
            if not node: return True
            # 2. check node value in range
            if not (left < node.val < right): return False
            # 3. make recursive call with update ranges
            left = dfs(node.left, left, node.val)
            right = dfs(node.right, node.val, right)
            return left and right
        
        return dfs(root, float("-inf"), float("inf"))