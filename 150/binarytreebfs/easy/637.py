# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        # 0. base case
        if not root: return []

        res = []
        # 1. use bfs algo with deque
        q = deque()
        q.append(root)

        while q:
            # 2. keep track of running sum and length of tree level
            total = 0.0
            n = len(q)
            # 3. compute sum of level
            for _ in range(n):
                node = q.popleft()
                # 4. add node children if they exist
                total += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            # 5. compute and add avg to res
            res.append(total / n)
        
        return res