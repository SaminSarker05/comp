# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        # 1. store all root to leaf strings in list
        store = []
        def dfs(root, path):
            if not root: return
            # 2. add to least when leaf node found
            if not root.left and not root.right:
                path += chr(root.val + 97)
                # 3. add to store in reverse order
                store.append(path[::-1])
            # 4. call left and right sides with char of current node
            dfs(root.left, path + chr(root.val + 97))
            dfs(root.right, path + chr(root.val + 97))
        dfs(root, "")
        # 5. return min in entire list
        return min(store)


      
