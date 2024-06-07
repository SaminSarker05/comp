# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # 0. dfs algo to make tree
        def dfs(array):
            # 1. base cases if one or 0 len array passed in
            if len(array) == 0: return
            if len(array) == 1: return TreeNode(array[0])

            # 2. choose mid of array as root of subtree
            # makes optimal height balanced trees
            mid = len(array) // 2

            # 3. make recursive calls with other halves of array
            root = TreeNode(array[mid])
            root.left = dfs(array[:mid])
            root.right = dfs(array[mid + 1: ])
            return root
        
        return dfs(nums)