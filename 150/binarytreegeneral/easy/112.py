# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.helper(root, 0, targetSum)

    def helper(self, node, running, target):
        if node is None: return False
        if node.left is None and node.right is None: 
            return running + node.val == target
        l = self.helper(node.left, running + node.val, target)
        r = self.helper(node.right, running + node.val, target)
        return l or r

"""
- recursion with helper method to track running sum
- if leaf node and running sum = target then found path
"""