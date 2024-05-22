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
        def recursive(node, flag):
            # 0. if NA node then return 0
            if not node: return 0
            
            # 1. only add to sum if leaf and left node
            if not node.left and not node.right and flag:
                return node.val
            
            # 2. mark as left side by passing flag
            return recursive(node.left, True) + recursive(node.right, False)
        
        return recursive(root, False)
