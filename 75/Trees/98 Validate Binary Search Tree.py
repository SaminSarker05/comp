# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def helper(node, left, right):
            if node is None:
                return True
            l = helper(node.left, left, node.val)
            r = helper(node.right, node.val, right)

            return l and r and left < node.val < right
        
        return helper(root, float("-inf"), float("inf"))