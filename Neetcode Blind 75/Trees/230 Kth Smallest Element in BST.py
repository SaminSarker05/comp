# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """


        self.k = k
        self.val = None
        self.helper(root)
        return self.val



    def helper(self, node):
        if not node:
            return
        # find smallest element by going as left as possible
        self.helper(node.left)
        # decrement k each time
        self.k -= 1
        # if found then keep returning and set val to answer
        if self.k == 0:
            self.val = node.val
            return
        # if kth num not found search right
        self.helper(node.right)
        