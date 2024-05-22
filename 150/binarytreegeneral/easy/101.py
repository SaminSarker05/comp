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
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if not left and not right: return True
        if not left and right or not right and left: return False
        if left.val != right.val:
            return False
        l = self.helper(left.left, right.right)
        r = self.helper(left.right, right.left)
        return l and r

"""
- helper function to pass left and right leafs
- helper compares corresponding leaves for symmetry
"""