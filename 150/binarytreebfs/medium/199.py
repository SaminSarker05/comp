# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root: return []

        res = []
        # 0. use queue for bfs algo to traverse tree
        q = deque()
        q.append(root)

        # 1. traverse tree by level
        while q:
            rightNode = None
            # 2. update rightNode after each removal in range
            for _ in range(len(q)):
                curr = q.popleft()
                # 3. if node has children add to queue
                rightNode = curr
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            # 4. add value of rightmost node to res
            res.append(rightNode.val)

        return res
        