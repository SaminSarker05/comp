# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        # 0. if depth to add at is first then create new node and simply point to root
        if depth == 1:
            res = TreeNode(val)
            res.left = root
            return res


        q = deque()
        q.append(root)
        level = 1
        # 1. BFS algo to traverse tree by later
        while q:
            # 2. when layer is desired depth add val to left and right sides
            if level == depth - 1:
                for _ in range(len(q)):
                    # 3. store existant left/right nodes to keep tree intact
                    node = q.popleft()
                    hold = node.left
                    node.left = TreeNode(val)
                    node.left.left = hold
    
                    hold = node.right
                    node.right = TreeNode(val)
                    node.right.right = hold
                break

            # 4. until found keep processing each layer
            for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
    
                    if node.right:
                        q.append(node.right)

            level += 1
        return root
            
