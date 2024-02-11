'''
time complexity: O(n) 
space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None:
            return

        val = False
        if root.val == subRoot.val:
            val =  self.check(root, subRoot)

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return l or r or val

    def check(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        l = self.check(root.left, subRoot.left)
        r = self.check(root.right, subRoot.right)

        return l and r