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

        # 0. base case
        if not root: return []

        # 1. BFS algo implementation
        q = deque()
        q.append(root)
        res = []

        while q:
            # 2. make temp array to hold level nodes
            running = []
            for _ in range(len(q)):
                # 3. if children add to queue
                node = q.popleft()
                running.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(running)

        return res