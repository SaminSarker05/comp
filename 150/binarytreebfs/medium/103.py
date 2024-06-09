# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # 0. base case
        if not root: return []

        res = []
        # 1. use queue for bfs algo
        q = deque()
        q.append(root)
        # 2. use flag to denote if normal or reverse order
        flag = True

        while q:
            running = []
            # 3. loop through current level of tree
            for _ in range(len(q)):
                node = q.popleft()
                # 4. add node children if they exists
                running.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            # 4. depending on flag add to res in reverse or normal order
            if flag: res.append(running)
            else: res.append(running[::-1])
            flag = not flag  # 5. negate flag each tree level

        return res