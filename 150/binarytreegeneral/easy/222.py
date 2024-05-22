# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        total = 0
        if root.left: total += self.countNodes(root.left)
        if root.right: total += self.countNodes(root.right)
        return total + 1

"""
- if left or right nodes exist than make recursive call
- sum # of nodes 
"""