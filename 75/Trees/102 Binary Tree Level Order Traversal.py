# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS search

        q = [root]
        res = []
        while q:
            level = []
            l = len(q)
            for _ in range(l):
                item = q.pop(0)
                if item:
                    level.append(item.val)
                    q.append(item.left)
                    q.append(item.right)
            
            if level != []:
                res.append(level)

        return res