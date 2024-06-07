# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = float("inf")
        self.prev = None

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 0. base case
        if not root: return 0

        # 1. inorder traversal of bst returns smallest to greatest
        def in_order(node):
            # 2. only make recursive call if left right nodes exist
            if node.left: in_order(node.left)
            # 3. update prev if does not exist
            if self.prev == None: self.prev = node.val
            # 4. if prev exists calculate difference with current and update res
            else: self.res = min(self.res, abs(node.val - self.prev))
            self.prev = node.val
            if node.right: in_order(node.right)

        in_order(root)
        return self.res