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
        self.res = None

        # 0. doing inorder traversal to go from smallest to greatest
        def in_order(node):
            if node.left: in_order(node.left)
            # 1. decrement k to know pos of node
            self.k -= 1
            # 2. if pos match then set res value
            if self.k == 0: 
                self.res = node.val
                return
            # 3. if left explored and k still not reach then explore right side
            if node.right: in_order(node.right)

        in_order(root)
        return self.res